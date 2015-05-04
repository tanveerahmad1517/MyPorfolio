from django.shortcuts import render, get_object_or_404
from .models import GalleryGroup, Artwork


def galleries(request):
    galleryGroups = GalleryGroup.objects.all().order_by('title')
    return render(request, 'gallery/galleries.html', { 'galleryGroups': galleryGroups })

def gallery_detail(request, gallery_title_slug):
    context_dict = {}
    
    try:
        galleryGroups = GalleryGroup.objects.get(slug=gallery_title_slug)
        context_dict['galleryGroups'] = galleryGroups
        artworks = Artwork.objects.filter(group=galleryGroups)
        context_dict['artworks'] = artworks

    except GalleryGroup.DoesNotExist:
        pass

    return render(request, 'gallery/gallery_detail.html', context_dict)

#def gallery_detail(request, pk):
 #   galleryGroups = get_object_or_404(GalleryGroup, pk=pk)
 #   artworks = Artwork.objects.filter(group=galleryGroups)
 #   return render(request, 'gallery/gallery_detail.html', 
 #       { 'galleryGroups': galleryGroups, 'artworks': artworks })

def art_detail(request, art_id):
    artwork = get_object_or_404(Artwork, id=art_id)
    return render(request, 'gallery/art_detail.html', {'artwork': artwork })
    
