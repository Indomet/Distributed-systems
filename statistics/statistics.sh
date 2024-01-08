#!/bin/bash

while true; do
    bookings=$(curl -s "http://192.168.96.193/api/v1/bookings/countAvailableBookings")
    users=$(curl -s "http://192.168.96.193/userCount")
  
    echo "Available Bookings:"
    echo "$bookings"

    echo "Online users:"
    echo "$users"

    sleep 3
done


# chmod +x statistics/statistics.sh
# ./statistics/statistics.sh


# chmod +x statistics.sh
# ./statistics.sh

