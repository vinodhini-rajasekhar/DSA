/* Write your T-SQL query statement below */
Select name as Customers from Customers where id NOT IN
(SELECT customerId FROM Orders)