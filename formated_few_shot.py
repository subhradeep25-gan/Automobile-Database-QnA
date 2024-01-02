examples = [
    {
        "Question": "What is the total quantity sold and revenue for each product in the 'Vintage Cars' product line?",
        "SQLQuery": """SELECT productName, SUM(quantityOrdered) as totalQuantity, SUM(priceEach * quantityOrdered) as totalRevenue 
                        FROM products 
                        JOIN orderdetails 
                        ON products.productCode = orderdetails.productCode 
                        WHERE productLine = 'Vintage Cars' 
                        GROUP BY productName 
                        ORDER BY tot""",
        "SQLResult":"Result of the SQL Query",
        "Answer": """The total quantity sold and revenue for each product in the 'Vintage Cars' product line is as follows: 
        1937 Lincoln Berline: 1111 quantity sold and 102563.52 revenue. 
        1936 Mercedes-Benz 500K Special Roadster: 960 quantity sold and 46078.29 revenue. 
        1917 Grand Touring Sedan: 918 quantity sold and 140535.60 revenue. 
        1911 Ford Town Car: 832 quantity sold and 45306.77 revenue. 
        1932 Model A Ford J-Coupe: 957 quantity sold and 109992.01 revenue."""
        },
    
    {
        "Question": "Retrieve the hierarchical structure of employees, including their names, job titles, and the office they belong to.",
        "SQLQuery": "SELECT firstName, lastName, jobTitle, city, phone, officeCode FROM employees LEFT JOIN offices USING (officeCode) LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The hierarchical structure of the employees includes Diane Murphy as President, Mary Patterson as VP Sales, Jeff Firrelli as VP Marketing, William Patterson as Sales Manager (APAC) in the Sydney Office, and Gerard Bondur as Sale Manager (EMEA) in the Paris Office."
    },
    
    {
        "Question":"List all customer orders, including customer information, order details, and the products ordered.",
        "SQLQuery": """SELECT c.customerName, c.contactLastName, c.contactFirstName, o.orderDate, o.requiredDate, o.shippedDate, o.status, o.comments,
		od.productCode, od.quantityOrdered, od.priceEach, 
		p.productName, p.productLine 
        FROM customers c 
        INNER JOIN orders o ON c.customerNumber = o.customerNumber 
        INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber 
        INNER JOIN products p ON od.productCode = p.productCode 
        LIMIT 5;""",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The first five customer orders, including customer information, order details, and the products ordered, are for Online Diecast Creations Co., ordered on January 6, 2003; Blauer See Auto, Co., ordered on January 9, 2003; etc."
        
    },
    {
        "Question":"Find the number of employees in each office, along with office details.",
        "SQLQuery": """SELECT offices.officeCode, offices.city, COUNT(employees.employeeNumber) AS numEmployees
        FROM offices
        INNER JOIN employees
        ON offices.officeCode=employees.officeCode
        GROUP BY offices.officeCode;""",
        "SQLResult":"Result of the SQL Query",
        "Answer": "There are 6 employees in San Francisco, 2 employees in Boston, 2 employees in NYC, 5 employees in Paris, 2 employees in Tokyo, 4 employees in Sydney, and 2 employees in London."
        
    },
    {
        "Question":"Retrieve customer information for those with a credit limit greater than $50,000.",
        "SQLQuery": "SELECT `customerNumber`, `customerName`, `contactLastName`, `contactFirstName`, `postalCode`, `country` FROM customers WHERE `creditLimit` > 50000 LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "Customers with a credit limit greater than $50,000 are Signal Gift Stores, Australian Collectors, Co., La Rochelle Gifts, Baane Mini Imports, and Mini Gifts Distributors Ltd."
        
    },
    {
        "Question":"Show the details of products with a quantity in stock less than 50.",
        "SQLQuery": "SELECT `productCode`, `productName`, `quantityInStock` FROM `products` WHERE `quantityInStock` < 50",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The products with a quantity in stock less than 50 are 'S24_2000', '1960 BSA Gold Star DBD34', with a quantity in stock of 15"
        
    },
    {
        "Question":"List all offices and the total number of employees in each office.",
        "SQLQuery": "SELECT `officeCode`, COUNT(*) AS 'num_employees' FROM employees GROUP BY `officeCode` ORDER BY `num_employees` DESC LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The offices with the highest number of employees are office 1 (6 employees), office 4 (5 employees), office 6 (4 employees), office 2 (2 employees) and office 3 (2 employees)."
        
    },
    {
        "Question":"Find the average credit limit for customers in the 'USA' country.",
        "SQLQuery": "SELECT AVG(creditLimit) FROM customers WHERE country = 'USA';",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The average credit limit for customers in the USA is 78102.777778."
        
    },
    {
        "Question":"Retrieve order details for orders placed on a specific date 2003-01-06.",
        "SQLQuery": "SELECT orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber FROM orderdetails WHERE orderNumber IN (SELECT orderNumber FROM orders WHERE orderDate = '2003-01-06');",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The order details for orders placed on 2003-01-06 are (10100, 'S18_1749', 30, Decimal('136.00'), 3), (10100, 'S18_2248', 50, Decimal('55.09'), 2), (10100, 'S18_4409', 22, Decimal('75.46'), 4), (10100, 'S24_3969', 49, Decimal('35.29'), 1)"
        
    },
    {
        "Question":"Show the total revenue generated from orders shipped to the 'Germany' country.",
        "SQLQuery": """SELECT SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS 'TotalRevenue'
        FROM orderdetails 
        INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber
        INNER JOIN customers ON orders.customerNumber = customers.customerNumber
        WHERE customers.country = 'Germany';""",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The total revenue generated from orders shipped to the 'Germany' country is 196,470.99."
        
    },
    {
        "Question":"Retrieve the product details and quantities ordered for a specific order number.",
        "SQLQuery": "SELECT productCode, productName, quantityOrdered, priceEach FROM orderdetails JOIN products USING (productCode) WHERE orderNumber = 10100;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The order number 10100 has the products 1917 Grand Touring Sedan, 1911 Ford Town Car, 1932 Alfa Romeo 8C2300 Spider Sport, and 1936 Mercedes Benz 500k Roadster with quantities ordered of 30, 50, 22, and 49 respectively."
        
    },
    {
        "Question":"List the products that have not been ordered yet.",
        "SQLQuery": "SELECT `productName` FROM productsWHERE `productCode` NOT IN (SELECT `productCode` FROM orderdetails);",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The product that has not been ordered yet is the 1985 Toyota Supra."
        
    },
    {
        "Question":"Find the top 5 customers with the highest credit limits.",
        "SQLQuery": "SELECT customerNumber, customerName, creditLimit FROM customers ORDER BY creditLimit DESC LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The top 5 customers with the highest credit limits are Euro+ Shopping Channel (227600.00), Mini Gifts Distributors Ltd. (210500.00), Vida Sport, Ltd (141300.00), Muscle Machine Inc (138500.00), and AV Stores, Co. (136800.00)."
        
    },
    {
        "Question":"Show the total revenue generated by each product line.",
        "SQLQuery": "SELECT productLine, SUM(quantityOrdered*priceEach) AS totalRevenue FROM orderdetails INNER JOIN products ON orderdetails.productCode = products.productCode GROUP BY productLine LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The total revenue generated by each product line is Classic Cars: $3.85M; Motorcycles: $1.12M; Planes: $954K; Ships: $663K; Trains: $188K."
        
    },
    {
        "Question":"Find the customers who have placed orders with a status of 'Shipped'.",
        "SQLQuery": "SELECT customerNumber FROM orders WHERE status = 'Shipped' LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The customers who have placed orders with a status of 'Shipped' are customer numbers 363, 128, 181, 121, and 141."
        
    },
    {
        "Question":"Show the products that have not been assigned to any product line.",
        "SQLQuery": "SELECT productCode, productName FROM products WHERE productLine = ''",
        "SQLResult":"Result of the SQL Query",
        "Answer": "There are no products that have not been assigned to a product line."
        
    },
    {
        "Question":"List the customers who have made payments with check numbers starting with 'CH'.",
        "SQLQuery": "SELECT customerNumber, checkNumber, paymentDate, amount FROM payments WHERE checkNumber LIKE 'CH%';",
        "SQLResult":"Result of the SQL Query",
        "Answer": "103, CH445585, 2003-08-15, 64663.78; 103, CH456223, 2004-12-31, 60694.78; 181, CH493774, 2004-12-01, 30253.75"
        
    },
    {
        "Question":"Find the average quantity ordered for each product.",
        "SQLQuery": "SELECT productCode, AVG(quantityOrdered) FROM orderdetails GROUP BY productCode LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The average quantity ordered for S10_1678 is 37.75, S10_1949 is 34.32, S10_2016 is 35.68, S10_4698 is 35.18, and S10_4757 is 36.79."
        
    },
    {
        "Question":"Retrieve the total number of orders placed each year.",
        "SQLQuery": "SELECT YEAR(`orderDate`) AS OrderYear, COUNT(`orderNumber`) AS NumberOfOrders FROM orders GROUP BY OrderYear ORDER BY OrderYear ASC LIMIT 5",
        "SQLResult":"Result of the SQL Query",
        "Answer": "In 2003, 111 orders were placed. In 2004, 151 orders were placed. In 2005, 64 orders were placed."
        
    },
    {
        "Question":"Show the products and their quantities ordered for orders shipped after a specific date 2003-01-06.",
        "SQLQuery": """SELECT products.productName, orderdetails.quantityOrdered 
        FROM orderdetails 
        INNER JOIN products ON orderdetails.productCode = products.productCode 
        INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber 
        WHERE orders.shippedDate > '2003-01-06'
        LIMIT 5;""",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The products and their quantities ordered for orders shipped after 2003-01-06 are: 1917 Grand Touring Sedan (30), 1911 Ford Town Car (50), 1932 Alfa Romeo 8C2300 Spider Sport (22), 1936 Mercedes Benz 500k Roadster (49), and 1932 Model A Ford J-Coupe (25)."
        
    },
    {
        "Question":"Retrieve the average credit limit for customers in each country.",
        "SQLQuery": "SELECT country, AVG(creditLimit) as avgCredit FROM customers GROUP BY country ORDER BY avgCredit DESC LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The average credit limit for customers in Denmark is 102100.00, in Italy is 97200.00, in Norway is 95950.00, in Finland is 95266.67 and in New Zealand is 90625.00."
        
    },
    {
        "Question":"Find the total revenue generated from orders placed by a specific sales representative.",
        "SQLQuery": "SELECT SUM(od.quantityOrdered * od.priceEach) AS 'totalRevenue' FROM orderdetails od INNER JOIN orders o ON od.orderNumber = o.orderNumber INNER JOIN customers c ON o.customerNumber = c.customerNumber WHERE c.salesRepEmployeeNumber = '1370';",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The total revenue generated from orders placed by this sales representative is $1,258,577.81"
        
    },
    {
        "Question":"Retrieve the details of customers who have not placed any orders.",
        "SQLQuery": "SELECT c.customerNumber, c.customerName FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber WHERE o.orderNumber IS NULL LIMIT 5;",
        "SQLResult":"Result of the SQL Query",
        "Answer": "The customers who have not placed any orders are 125 - Havel & Zbyszek Co, 168 - American Souvenirs Inc, 169 - Porto Imports Co., 206 - Asian Shopping Network, Co, and 223 - Natürlich Autos."
        
    },
    
]