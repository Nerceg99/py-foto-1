from PIL import Image


algebra_campus = 'algebra_campus.jpg'
algebra_news = 'algebra.jpg'
photo_algebra_campus = Image.open(algebra_campus)
photo_algebra_news = Image.open(algebra_news)

print(f'Velicina fotografije Algebra Campus je: {photo_algebra_campus.size}.')
print(f'Velicina fotografije Algebra News je: {photo_algebra_news.size}.')

photo_algebra_news = photo_algebra_news.convert(mode='L')


photo_algebra_campus.show()
photo_algebra_news.show()
