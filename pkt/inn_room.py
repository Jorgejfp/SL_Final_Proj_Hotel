import mysql.connector
from pkt.connection import connectDB

class Room:
    def __init__(self, room_type, room_price, availability):
            self.id = None
            self.room_type = room_type
            self.room_price = room_price
            self.availability = availability
            
    def getID(room_type):
        try:
            # Connect to the database
            connRoomDB = connectDB()

            # Create a cursor object to execute SQL queries
            cursor = connRoomDB.cursor()

            # Prepare the SQL query to retrieve the ID of a room based on room_type
            query = "SELECT id FROM inn_rooms WHERE room_type = %s"
            values = (room_type,)

            # Execute the query
            cursor.execute(query, values)

            # Fetch the result
            room_type = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()

            return room_type
        except mysql.connector.Error as error:
            print(f"Failed to get room ID: {error}")
            return None
    
    def list_rooms():   
        
        connRoomDB = connectDB()
        cursor = None
        try:
            if connRoomDB is not None:
                # Create a cursor object to execute SQL queries
                cursor = connRoomDB.cursor()
                # Prepare the SQL query to retrieve all rooms
                query = "SELECT * FROM inn_rooms"
                # Execute the query
                cursor.execute(query)
                # Fetch all the results
                rooms = cursor.fetchall()
                #Display the results
                print("List of rooms:")
                print("{:<10} {:<10} {:<10} {:<10}".format("ID", "Room Type", "Price", "Availability"))
                for room in rooms:
                    Room.print_room_details(room)                  
            else:
                print("Connection to database failed")
        except Exception as e:
            print(f"Failed to list rooms: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connRoomDB is not None:
                connRoomDB.close()        
                
    
    def decrease_availability(self):
        try:
            # Connect to the database
            connRoomDB = connectDB()

            # # Create a cursor object to execute SQL queries
            # cursor = connRoomDB.cursor()

            # # Prepare the SQL query to decrease the availability of a room
            # query = "UPDATE inn_rooms SET availability = availability - 1 WHERE id = %s"
            # values = (self,)

            # # Execute the query
            # cursor.execute(query, values)

            # # Commit the changes to the database
            # connRoomDB.commit()

            # # Close the cursor and connection
            # cursor.close()
            
            if connRoomDB is not None: 
                
                # Create a cursor object to execute SQL queries
                cursor = connRoomDB.cursor()                
                # Prepare the SQL query to decrease the availability of a room
                query = "UPDATE inn_rooms SET availability = availability - 1 WHERE id = %s"
                values = (self,)

                # Execute the query
                cursor.execute(query, values)

                # Commit the changes to the database
                connRoomDB.commit()
            else:
                print("Connection to database failed")   
        except Exception as e:
            print(f"Failed to decrease room availability:: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connRoomDB is not None:
                connRoomDB.close()                   

    def increase_availability(self):
        
        connRoomDB = connectDB()
        cursor = None
        try:
            
            if connRoomDB is not None: 
            
                # Create a cursor object to execute SQL queries
                cursor = connRoomDB.cursor()
                # Prepare the SQL query to increase the availability of a room
                query = "UPDATE inn_rooms SET availability = availability + 1 WHERE id = %s"
                values = (self,)

                # Execute the query
                cursor.execute(query, values)

                # Commit the changes to the database
                connRoomDB.commit()       
                        
            else:
                print("Connection to database failed")   
        except Exception as e:
            print(f"Failed to increase room availability:: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connRoomDB is not None:
                connRoomDB.close()  
                    
    def get_total_available_rooms():
        try:
            # Connect to the database
            connRoomDB = connectDB()

            # Create a cursor object to execute SQL queries
            cursor = connRoomDB.cursor()

            # Prepare the SQL query to retrieve the total available rooms
            query = "SELECT COUNT(*) FROM rooms WHERE room_availability > 0"

            # Execute the query
            cursor.execute(query)

            # Fetch the result
            total_available_rooms = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
        

            return total_available_rooms
        except mysql.connector.Error as error:
            print(f"Failed to get total available rooms: {error}")                                      
    
    def check_availability(room_type):
        
        connRoomDB = connectDB()
        cursor = None
        try:
            if connRoomDB is not None:
                
                # Create a cursor object to execute SQL queries
                cursor = connRoomDB.cursor()

                # Prepare the SQL query to check the availability of a room based on room_type
                query = "SELECT availability FROM inn_rooms WHERE room_type = %s"
                values = (room_type,)

                # Execute the query
                cursor.execute(query, values)

                # Fetch the result
                availability = cursor.fetchone()
                
                if availability is not None:
                    return availability[0] 
                else:
                    print("there is no availability for this room type")
            else:
                print("Connection to database failed")
            
        except Exception as e:
                print(f"Failed to check room availability: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connRoomDB is not None:
                connRoomDB.close()
        
    @staticmethod
    def print_room_details(room):
        print("{:<10} {:<10} {:<10} {:<10}".format(*room))
            
                    
            