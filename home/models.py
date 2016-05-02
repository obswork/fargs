from django.db import models
from django.contrib import messages
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class Message(models.Model):
    # Why violate DRY in constructing choices? Check: https://docs.djangoproject.com/en/1.9/ref/models/fields/
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'
    CATEGORY_CHOICES = (
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
    )

    # blank=False is default but "Explicit is better than implicit."
    sender = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    number = models.CharField(max_length=20, null=True)
    message = models.TextField()
    category = models.CharField(max_length=15, blank=False, choices=CATEGORY_CHOICES, default="Residential")
    contact_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    contacted = models.BooleanField(default=False)

    # Python 2
    def __unicode__(self):
        return "{}".format(self.email)

    # Python 3
    def __str__(self):
        return "{}".format(self.email)


class HomePage(Page):

    # MAIN IMAGE MODELS
    header_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    parralax_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        blank=False,
        related_name='+'
    )

    # IMAGE EDITOR PANEL CONFIGS
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('header_background_image'),
                ImageChooserPanel('logo_image'),
                ImageChooserPanel('parralax_image'),
            ],
            heading="Main Images Editor",
            classname="collapsible collapsed"
        ),
    ]

    # HEADER MODELS
    header_text = RichTextField(blank=False)
    header_button = models.CharField(max_length=255, blank=False)

    # HEADER EDITOR PANEL CONFIGS
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('header_text', classname="full"),
                FieldPanel('header_button'),
            ],
            heading="Landing Page Editor",
            classname="collapsible collapsed"
        ),
    ]

    # SECTION 1 MODELS
    s1_text = RichTextField()
    s1_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        blank=False,
        related_name='+'
    )

    # SECTION 1 EDITOR PANEL CONFIGS
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('s1_text', classname="full"),
                ImageChooserPanel('s1_image'),
            ],
            heading="Row 1 Editor",
            classname="collapsible collapsed"
        ),
    ]

    # SECTION 2 MODELS (not incl. foreign Icon models)
    s2_text = RichTextField()

    # SECTION 2 EDITOR PANEL CONFIGS
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('s2_text', classname="full"),
                InlinePanel('icons', label="Icons"),
            ],
            heading="Row 2 Editor",
            classname="collapsible collapsed"
        ),
    ]

    # SECTION 3 MODELS
    s3_text = RichTextField()
    service1 = models.CharField(max_length=255, blank=False)
    service2 = models.CharField(max_length=255, blank=False)
    service2_price = models.IntegerField(default=289)

    # SECTION 3 EDITOR PANEL CONFIGS
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('s3_text', classname="full"),
                FieldPanel('service1'),
                FieldPanel('service2'),
                FieldPanel('service2_price'),
            ],
            heading="Services Editor",
            classname="collapsible collapsed"
        ),
    ]

    # for now services hardcoded in html (css alignment for the bullet-items annoying to deal with

    # SECTION 4 MODELS
    s4_text = RichTextField()

    # SECTION 4 EDITOR PANEL CONFIGS
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('s4_text', classname="full"),
            ],
            heading="Call-to-Action Editor",
            classname="collapsible collapsed"
        ),
    ]

    def serve(self, request):
        from home.forms import MessageForm
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "Thanks for your message, our staff will contact you shortly.")
                form = MessageForm()
                return render(request, 'home/home_page.html', {
                    'page': self,
                    'form': form,
                })

                return render(request, 'home/home_page.html', {
                    'page': self,
                    'form': form,
                })

            form = MessageForm()

            messages.error(request, "Whoops, try again.")
            return render(request, 'home/home_page.html', {
                'page': self,
                'form': form,
                })

        else:
            form = MessageForm()

        return render(request, 'home/home_page.html', {
            'page': self,
            'form': form,
            })


class Icon(Orderable):
    page = ParentalKey(HomePage, related_name='icons')
    style = models.IntegerField()
    name = models.CharField(max_length=255)

    # Python 2
    def __unicode__(self):
        return "{}".format(self.name)

    # Python 3
    def __str__(self):
        return "{}".format(self.name)
