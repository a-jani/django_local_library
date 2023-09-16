from django.contrib import admin

# Register your models here.

from .models import Author,Genre,Book,Language,BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

###############################################################################################################
class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book
###############################################################################################################
#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines=[BooksInline]
#Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)
###############################################################################################################
class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance
###############################################################################################################
# Register the Admin classes for Book using the decorator
class BookAdmin(admin.ModelAdmin):

    def  display_genre(self):
         """Create a string for the Genre. This is required to display genre in Admin."""
         return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

    list_display = ('title', 'author', display_genre)

    inlines=[BooksInstanceInline]
    

admin.site.register(Book,BookAdmin)
###############################################################################################################
# Register the Admin classes for BookInstance using the decorator
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(BookInstance,BookInstanceAdmin)
