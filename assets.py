import pygame


class load:
    @staticmethod
    def image(path, **kwargs):
        path = f"assets/sprites/{path}"
        asset = pygame.image.load(path)
        if size := kwargs.get("size"):
            asset = pygame.transform.scale(asset, size)
        if kwargs.get("alpha"):
            return asset.convert_alpha()
        else:
            return asset.convert()
        return s


class scale:
    @staticmethod
    def image(img: pygame.Surface, scale_factor: int):
        w, h = img.get_size()
        return pygame.transform.scale(img, (w * scale_factor, h * scale_factor))
