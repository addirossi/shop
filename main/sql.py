#SELECT, INSERT, UPDATE, DELETE


# SELECT * FROM product;
# Product.objects.all()

# SELECT id, name FROM product;
# Product.objects.only('id', 'name')

# SELECT description, price, category_id FROM product;
# Product.objects.defer('id', 'name')

# SELECT * FROM product WHERE price > 50000;
# Product.objects.filter(price__gt=50000)

# SELECT * FROM product WHERE price = 50000;
# Product.objects.filter(price=50000)

# SELECT * FROM product WHERE price < 50000;
# Product.objects.filter(price__lt=50000)

# SELECT * FROM product WHERE price != 50000;
# Product.objects.exclude(price=50000)
# Product.objects.filter(~Q(price=50000))

# SELECT * FROM product WHERE price <= 50000;
# Product.objects.filter(price__lte=50000)

# SELECT * FROM product WHERE price >= 50000;
# Product.objects.filter(price__gte=50000)

# SELECT * FROM product WHERE price BETWEEN 50000 AND 60000;
# Product.objects.filter(price__range=[50000, 60000])

# SELECT * FROM product WHERE price >= 50000 AND price <= 60000;
# Product.objects.filter(price__gte=50000).filter(price__lte=60000)
# Product.objects.filter(price__gte=50000, price__lte=60000)

# SELECT * FROM product WHERE category_id IN ('smartphones', 'accessories');
# Product.objects.filter(category_id__in=['smartphones', 'accessories'])

# SELECT * FROM product WHERE category_id = 'smartphones' OR category_id = 'accessories';
# Product.objects.filter(Q(category_id='smartphones')|Q(category_id='accessories'))

# LIKE
# ILIKE

# SELECT * FROM product WHERE name LIKE 'Samsung%';
# Product.objects.filter(name__startswith='Samsung')

# SELECT * FROM product WHERE name ILIKE 'Samsung%';
# Product.objects.filter(name__istartswith='Samsung')

# SELECT * FROM product WHERE name LIKE '%Samsung';
# Product.objects.filter(name__endswith='Samsung')

# SELECT * FROM product WHERE name ILIKE '%Samsung';
# Product.objects.filter(name__iendswith='Samsung')

# SELECT * FROM product WHERE name LIKE '%Samsung%';
# Product.objects.filter(name__contains='Samsung')

# SELECT * FROM product WHERE name ILIKE '%Samsung%';
# Product.objects.filter(name__icontains='Samsung')

# SELECT * FROM product WHERE name LIKE 'Samsung';
# Product.objects.filter(name__exact='Samsung')

# SELECT * FROM product WHERE name ILIKE 'Samsung';
# Product.objects.filter(name__iexact='Samsung')

#ORDER_BY

# SELECT * FROM product ORDER BY price ASC;
# Product.objects.order_by('price')

# SELECT * FROM product ORDER BY price DESC;
# Product.objects.order_by('-price')

# COUNT

# SELECT COUNT(*) FROM product;
# Product.objects.count()

# SELECT COUNT(*) FROM product WHERE category_id = 'smartphones';
# Product.objects.filter(category_id='smartphones').count()

#INSERT
# INSERT INTO product (...) VALUES (...);
# Product.objects.create(name='...', description='...', price=..., category=...)

# product = Product(name='...', description='...', price=..., category=...)
# product.save()

#
# INSERT INTO product (...) VALUES (...), (...), (...);
# Product.objects.bulk_create([
#     Product(name='...', description='...', price=..., category=...),
#     Product(name='...', description='...', price=..., category=...),
#     Product(name='...', description='...', price=..., category=...)
# ])

# UPDATE
# UPDATE product SET price = price - 5000;
# Product.objects.update(price=F(price) - 5000)

# UPDATE product SET price = price - 4000 WHERE price > 50000;
# Product.objects.filter(price__gt=50000).update(price=F(price) - 4000)


# UPDATE product SET price = 51000 WHERE id=2;
# Product.objects.filter(id=2).update(price=51000)

# product = Product.objects.get(id=2)
# product.price = 51000
# product.save()

# DELETE

# DELETE FROM product;
# Product.objects.delete()

# DELETE FROM product WHERE category_id = 'accessories';
# Product.objects.filter(category_id='accessories').delete()

# DELETE FROM product WHERE id=2;
# Product.objects.filter(id=2).delete()

# product = Product.objects.get(id=2)
# product.delete()

