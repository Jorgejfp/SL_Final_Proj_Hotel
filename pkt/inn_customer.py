import mysql.connector
from pkt.connection import connectDB

class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    
    def save_to_dbCustomer(self):
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        if connCustomerDB is not None:
            try:
            
                # Create a cursor object to execute SQL queries
                cursor = connCustomerDB.cursor()
                # Prepare the SQL query to insert customer data into the table
                query = "INSERT INTO inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
                values = (self.first_name, self.last_name, self.email, self.phone_number)
                # Execute the SQL query
                cursor.execute(query, values)
                # Commit the changes to the database
                connCustomerDB.commit()
                print("Customer data saved successfully!")
            except Exception as e:
                print(f"Error when saving customer data: {e}")
                connCustomerDB.rollback() # Rollback the changes if an error occurs
            finally:
                # Close the cursor and database connection
                cursor.close()
                connCustomerDB.close()
        else:    
            print("Error: Could not connect to database")
        
    def update_in_dbCustomer(self):
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = connCustomerDB.cursor()
        # Prepare the SQL query to update customer data in the table
        query = "UPDATE inn_customer SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE id = %s"
        values = (self.first_name, self.last_name, self.email, self.phone_number, self.id)
        # Execute the SQL query
        cursor.execute(query, values)
        # Commit the changes to the database
        connCustomerDB.commit()
        # Close the cursor and database connection
        cursor.close()
        
    def list_customers():
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        cursor = None  # Initialize cursor to None outside the try block
        try:
            # Check if the connection has been successfully established 
            if connCustomerDB is not None:
                    # Create a cursor object to execute SQL queries
                    cursor = connCustomerDB.cursor()
                    # Prepare the SQL query to select all customers from the table
                    query = "SELECT * FROM inn_customer"
                    # Execute the SQL query
                    cursor.execute(query)
                    # Fetch all the rows returned by the query
                    customers = cursor.fetchall()
                    print("\nCustomer Details:\n")
                    print("{:<10} {:<15} {:<15} {:<30} {:<15}".format("ID", "First Name", "Last Name", "Email", "Phone Number"))
                    for customer in customers:
                        Customer.print_customer_details(customer)
                        #print(customer) # Print each customer record
                    input("\nPress Enter to continue...")
            else:
                print("Error: Could not connect to database")
        except Exception as e:
                    print(f"Error when listing customers: {e}")  
        finally:
            # Close the cursor and the connection to the database if the cursor has been initialized correctly
            if cursor is not None: 
                cursor.close()
            if connCustomerDB is not None:
                connCustomerDB.close()
                
                
                
    def delete_customer_by_id(customer_id):
        # Connect to the database
        connCustomerDB = connectDB()
        cursor = None
        try:
            if connCustomerDB is not None:
                cursor = connCustomerDB.cursor()
                
                # Check if the customer ID exists in the database
                query = "SELECT first_name, last_name, email, phone_number FROM inn_customer WHERE id = %s"
                cursor.execute(query, (customer_id,))
                customer_data = cursor.fetchone()
                if customer_data is not None:
                    # Delete the customer directly using the fetched customer ID
                    query_delete = "DELETE FROM inn_customer WHERE id = %s"
                    cursor.execute(query_delete, (customer_id,))
                    connCustomerDB.commit()
                    print("Customer with ID {} deleted successfully!".format(customer_id))
                else:
                    print("Customer with ID {} does not exist.".format(customer_id))                                
            else:
                print("Error: Could not connect to database")
        except Exception as e:
            print(f"Error when deleting customer data: {e}")
            if connCustomerDB is not None:
                connCustomerDB.rollback()  # Rollback the changes if an error occurs
        finally:
            if cursor is not None:
                cursor.close()
            if connCustomerDB is not None:
                connCustomerDB.close()
                
    def get_customer_by_id(customer_id):
        try:
            # Connect to the database
            connCustomerDB = connectDB()
            cursor = None
            if connCustomerDB is not None:
                cursor = connCustomerDB.cursor()
                # Prepare the SQL query to select the customer by ID
                query = "SELECT first_name,last_name,email,phone_number FROM inn_customer WHERE id = %s"
                cursor.execute(query, (customer_id,))
                customer_data = cursor.fetchone()
                if customer_data is not None:
                    # Create a Customer object from the fetched data
                    customer = Customer(*customer_data)
                    return customer
                else:
                    print("Customer with ID {} does not exist.".format(customer_id))
            else:
                print("Error: Could not connect to database")
        except Exception as e:
            print(f"Error when fetching customer data: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connCustomerDB is not None:
                connCustomerDB.close()
                
    def print_customer_details2(self):
        #print("Customer ID:", self.id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)
        
    @staticmethod            
    def print_customer_details(customer):
        print("{:<10} {:<15} {:<15} {:<30} {:<15}".format(*customer))