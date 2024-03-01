import settings

def height_percnt(percent):
    return (settings.HEIGHT/100)*percent
def width_percnt(percent):
    return (settings.WIDTH/100)*percent
print(height_percnt(25))