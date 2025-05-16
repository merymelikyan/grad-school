from django.db import models


class Header(models.Model):
    title1 = models.CharField(max_length=55, null=True, blank=True)
    title2 = models.CharField(max_length=55, null=True, blank=True)
    icon_class= models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    link_url1 = models.CharField(max_length=200, null=True, blank=True) 
    link_url2 = models.CharField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return f"{self.title1} | {self.title2}"
    
    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Header"   


class SectionsMenu(models.Model):
    section_id = models.CharField(max_length=100,unique=True, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    link_name = models.TextField(max_length=55, null=True, blank=True)
    link_url = models.CharField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Sections Menu"
        verbose_name_plural = "Sections Menu"   


class MenuItem(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    href = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
    


class MainBanner(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    text1 = models.CharField(max_length=55, null=True, blank=True)
    text2 = models.CharField(max_length=55, null=True, blank=True)
    video_file = models.FileField(upload_to='videos/', db_index=True, null=True, blank=True)
    link_name = models.TextField(max_length=55, null=True, blank=True)
    link_url = models.CharField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Main Banner"
        verbose_name_plural = "Main Banner"   


class Features(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.CharField(max_length=500, null=True, blank=True)
    description2 = models.CharField(max_length=500, null=True, blank=True)
    icon_class= models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    link_name = models.CharField(max_length=55, null=True, blank=True)
    link_url = models.CharField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Features"
        verbose_name_plural = "Features"    



class BlockNames(models.Model):
    title = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = "Block Names"
        verbose_name_plural = "Block Names"   


class Choosetab(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link_url = models.CharField(max_length=200, blank=True, null=True) 
   
    def __str__(self):
        return  self.title
    
    class Meta:
        verbose_name = "Choosetab"
        verbose_name_plural = "Choosetab" 


class Tabs(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    tabs_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description1 = models.CharField(max_length=500, null=True, blank=True)
    description2 = models.CharField(max_length=500, null=True, blank=True)
    description3 = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="image", blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tabs"
        verbose_name_plural = "Tabs"    



class ComingSoon(models.Model):
    title1 = models.CharField(max_length=100, blank=True, null=True)
    title2 = models.CharField(max_length=100, blank=True, null=True)
    title3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title1} | {self.title2}"
    
    class Meta:
        verbose_name = "Coming Soon"
        verbose_name_plural = "Coming Soon"    


class Time(models.Model):
    class_name = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.class_name
    
    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"    


class Registration(models.Model):
    title1 = models.CharField(max_length=100, null=True, blank=True)
    title2 = models.CharField(max_length=100, null=True, blank=True)
    title3 = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phon_number = models.CharField(max_length=100, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.name}"
    
    class Meta:
        verbose_name = "Registration"
        verbose_name_plural = "Registration"



class Section_courses(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(max_length=50, null=True, blank=True)
    image1 = models.ImageField(upload_to="courses", blank=True, null=True)
    image2 = models.ImageField(upload_to="author", blank=True, null=True)
    icon_class= models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    link_url = models.CharField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Section_courses"
        verbose_name_plural = "Section_courses"    


class Section_video(models.Model):
    tag = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100, blank=True, null=True)
    title2 = models.CharField(max_length=100, blank=True, null=True)
    description1 = models.TextField(max_length=500, null=True, blank=True)
    description2 = models.TextField(max_length=500, null=True, blank=True)
    description3 = models.TextField(max_length=500, null=True, blank=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_url1 = models.URLField(max_length=200, blank=True, null=True) 
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=200, blank=True, null=True) 
    video_name = models.TextField(max_length=50, null=True, blank=True)
    video_url = models.URLField(db_index=True, null=True, blank=True)
    image = models.ImageField(upload_to="main", blank=True, null=True)
   
    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = "Section_video"
        verbose_name_plural = "Section_video"    

      
                
class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.name}"
    

class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True)
    link_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"    