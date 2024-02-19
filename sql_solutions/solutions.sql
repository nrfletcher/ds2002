/* Query 1 */
select actor.first_name, actor.last_name from film 
	inner join film_actor on film.film_id = film_actor.film_id
  inner join actor on film_actor.actor_id = actor.actor_id
  where film.title = 'ACADEMY DINOSAUR';

/* Query 2 */
select category.name, count(film_category.category_id) from category 
	inner join film_category on category.category_id = film_category.category_id
  inner join film on film_category.film_id = film.film_id
  group by category.name;

/* Query 3 */
select film.rating, avg(film.rental_duration) as avg_rental_duration
	from film
  group by film.rating;

/* Query 4 */
select customer.first_name, customer.last_name, count(rental.customer_id) as rental_count
	from customer
  join rental on customer.customer_id = rental.customer_id
  group by customer.first_name, customer.last_name;

/* Query 5 */
select store.store_id, count(rental.rental_id) as rental_count
	from store
  join inventory on store.store_id = inventory.store_id
  join rental on inventory.inventory_id = rental.inventory_id
  group by store.store_id
  order by rental_count desc
  limit 1;

/* Query 6 */
select category.name, count(rental.rental_id) as rental_count
	from category
  join film_category on category.category_id = film_category.category_id
  join film on film_category.film_id = film.film_id
  join inventory on film.film_id = inventory.film_id
  join rental on inventory.inventory_id = rental.inventory_id
  group by category.name;

/* Query 7 */
select category.name, avg(film.rental_rate) as avg_rental_rate
	from category
  join film_category on category.category_id = film_category.category_id
  join film on film_category.film_id = film.film_id
  group by category.name;

/* Query 8 */
select film.title, max(rental.rental_date) as latest_rental_date
	from film
  join inventory on film.film_id = inventory.film_id
  join rental on inventory.inventory_id = rental.inventory_id
  group by film.title;

/* Query 9 */
select customer.first_name, customer.last_name, sum(payment.amount) as total
	from payment
  join customer on payment.customer_id = customer.customer_id
  group by customer.first_name, customer.last_name;

/* Query 10 */
select language.name, avg(film.length) as duration
	from film
  join language on film.language_id = language.language_id
  group by language.name;

