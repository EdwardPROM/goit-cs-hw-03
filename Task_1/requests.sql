--Отримати всі завдання певного користувача.
SELECT * FROM tasks WHERE user_id = 76;

--Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select * from tasks where status_id =(select  id from status where name='new');

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE tasks set  status_id = (SELECT id FROM status WHERE name='in progress') WHERE id=31;
SELECT * FROM tasks WHERE id=31;

--Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
select * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

--Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Створити звіт', 'Звіт за травень місяць', 1, 75);
SELECT * FROM tasks where title='Створити звіт';

--Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.

SELECT * FROM TASKS WHERE status_id <> (SELECT id FROM status WHERE name='completed');

--Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.

DELETE FROM tasks WHERE id=12;

--Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.

SELECT * FROM users WHERE email like 'a%';

--Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.

UPDATE users set fullname='Jacob Byrd' WHERE id=27;
SELECT * FROM users WHERE id=27;

--Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.

SELECT s.name, count(1) FROM tasks t join status s on t.status_id=s.id GROUP BY s.name;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').

select * from tasks t join users u on t.user_id=u.id where u.email like '%@example.com';

--Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.

update tasks set description = null where id=28;
select * from tasks where description is null;

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.

select * from tasks t join users u on t.user_id=u.id inner join status s on t.status_id=s.id where s.name ='in progress';

--Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.

SELECT u.fullname, g.task_count  FROM users u
LEFT join (select user_id, count(1) task_count from tasks  
GROUP BY user_id) g on u.id=g.user_id;