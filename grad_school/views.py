from django.contrib import messages
from django.shortcuts import render, get_object_or_404


from .models import (
    Header,
    SectionsMenu,
    MenuItem,
    MainBanner,
    Features,
    BlockNames,
    Choosetab,
    Tabs,
    ComingSoon,
    Time,
    Registration,
    Section_courses,
    Section_video,
    Contact,
    FooterText
)


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phon_number = request.POST.get("phon_number", "")
        message = request.POST.get("message")

        Registration.objects.create(
            full_name=name,
            email=email,
            phon_number=phon_number,
            message=message
        )

        messages.success(request, "You are registrated successfully !")


    header = Header.objects.all().first()
    sections_menu = SectionsMenu.objects.all()
    menu_item = MenuItem.objects.all()
    main_banner = MainBanner.objects.all().first()
    features = Features.objects.all()
    block_names = BlockNames.objects.all()
    choose_tab = Choosetab.objects.all()
    tabs = Tabs.objects.all()
    coming_soon = ComingSoon.objects.all().first()
    time = Time.objects.all()
    section_courses = Section_courses.objects.all()
    section_video = Section_video.objects.all().first()
    contact = Contact.objects.first()
    footer_text = FooterText.objects.all().first()


    data = {
        "header": header,
        "sections_menu": sections_menu,
        "menu_item": menu_item,
        "main_banner": main_banner,
        "features": features,
        "block_names": block_names,
        "choose_tab": choose_tab,
        "tabs": tabs,
        "coming_soon": coming_soon,
        "time": time,
        "section_courses": section_courses,
        "section_video": section_video,
        "contact": contact,
        "footer_text": footer_text
    }
    

    return render(request,"base.html", data)