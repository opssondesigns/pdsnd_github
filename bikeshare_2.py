import time as time

import pandas as pd

import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',

'new york city': 'new_york_city.csv',

'washington': 'washington.csv' }

months = {'january', 'february', 'march', 'april', 'may', 'june','all'}

days = {1,2,3,4,5,6,7,8}

#================FUNCTION1=================================
def get_filters():

   """

   Asks user to specify a city, month, and day to analyze.

   Returns:

   (str) city - name of the city to analyze

   (str) month - name of the month to filter by, or "all" to apply no month filter

   (str) day - name of the day of week to filter by, or "all" to apply no day filter

   """

   print('Hello! Let\'s explore some US bikeshare data!')

   while True:

      city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()

      if city not in CITY_DATA:

         print("Sorry, {} is not a valid city. Please type again by entering either 'Chicago', 'New York City' OR 'Washington'".format(city))

         continue

      else:

         break
      #print('Welcome')

   while True:

      month = input("Which month? January, February, March, April or June?\n").lower()

      if month not in months:

         print("Sorry, {} is not a valid month. Please type again".format(month))

      else:

         break
   while True:

      day = int(input("Which day(Enter 8 for 'all')? Enter the response in integer. Ex: 1 = Sunday\n"))

      if day not in days:

         print("Sorry, {} is not a valid day. Please type again by entering the day of week in integer".format(day))

      else:

         break

      print("You have chosen: ",city," ", month," ", day," ")

      print('-'*40)

   return city, month, day
#================FUNCTION2=================================

def load_data(city, month, day):

   """

   Loads data for the specified city and filters by month and day if applicable.

   Args:

   (str) city - name of the city to analyze

   (str) month - name of the month to filter by, or "all" to apply no month filter

   (str) day - name of the day of week to filter by, or "all" to apply no day filter

   Returns:

   df - Pandas DataFrame containing city data filtered by month and day

   """

   df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime

   df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns

   df['month'] = df['Start Time'].dt.month

   df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month if applicable

   if month != 'all':

      months = ['january', 'february', 'march', 'april', 'may', 'june']

      month = months.index(month) + 1

# filter by month to create the new dataframe

   df = df[df['month'] == month]

# filter by day of week if applicable

   if day != 'all':

#filter by day of week to create the new dataframe

      df = df[df['day_of_week'] == day.title()]

   return df
#================FUNCTION3=================================

def time_stats(df):

   """Displays statistics on the most frequent times of travel."""

   print('\nCalculating The Most Frequent Times of Travel...\n')

   start_time = time.time()

   df = pd.read_csv(CITY_DATA[city])

   df['Start Time'] = pd.to_datetime(df['Start Time'])

   df['month'] = df['Start Time'].dt.month

   common_month = df['month'].mode()[0]

   print('Most common month: ', common_month)

   df = pd.read_csv(CITY_DATA[city])

   df['Start Time'] = pd.to_datetime(df['Start Time'])

   df['week_day'] = df['Start Time'].dt.weekday_name

   common_day_of_week = df['week_day'].mode()[0]

   print('Most common day of the week: ', common_day_of_week)

   df = pd.read_csv(CITY_DATA[city])

   df['Start Time'] = pd.to_datetime(df['Start Time'])

   df['hour'] = df['Start Time'].dt.hour

   start_hour = df['hour'].mode()[0]

   print('Most common hour of the day: ', start_hour)

   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*40)
#================FUNCTION4=================================

def station_stats(df):

   """Displays statistics on the most popular stations and trip."""

   print('\nCalculating The Most Popular Stations and Trip...\n')

   start_time = time.time()

   start_st = df['Start Station'].mode()[0]

   print('Most Common start station: ', start_st)

   end_st = df['End Station'].mode()[0]

   print('Most Common End station: ', end_st)

   df['comb'] = df['Start Station'] + ' to ' + df['End Station']

   common_combo = df['comb'].mode()[0]

   print('Most common combination of Start and End station: ',common_combo)

   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*40)
#================FUNCTION5=================================

def trip_duration_stats(df):

   """Displays statistics on the total and average trip duration."""

   print('\nCalculating Trip Duration...\n')

   start_time = time.time()

   trip_dur = df['Trip Duration'].sum()

   print('Total trip duration: ',trip_dur)

   mean_travel = df['Trip Duration'].mean()

   print('Mean Travel Time: ',mean_travel)

   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*40)
#================FUNCTION6=================================

def user_stats(df):

   """Displays statistics on bikeshare users."""

   print('\nCalculating User Stats...\n')

   start_time = time.time()

   user_types = df['User Type'].value_counts()

   print('Count of User types: ',user_types)

   if 'Gender' in df:

      gender_count = df['Gender'].value_counts()

      print('Total Gender count: ',gender_count)

   else:

      print('Gender information is not available for this city')

   if 'Birth Year' in df:

      earliest_birth_year = df['Birth Year'].min()

      print('Earliest Birth Year: ',earliest_birth_year)

   else:

      print('Birth Year information is not available for this city')

   if 'Birth Year' in df:

      recent_birth_year = df['Birth Year'].max()

      print('Most recent Birth Year: ',recent_birth_year)

   else:

      print('Birth Year information is not available for this city')

   if 'Birth Year' in df:

      common_birth_year = df['Birth Year'].mode()[0]

      print('Most common Birth Year: ',common_birth_year)

   else:

      print('Birth Year information is not available for this city')

   print("\nThis took %s seconds." % (time.time() - start_time))

   print('-'*40)
#===================MAIN FUNCTION==================================

def main():

   while True:
#================INVOKING FUNCTIONS=================================
      city, month, day = get_filters()

      df = load_data(city, month, day)

      time_stats(df)

      station_stats(df)

      trip_duration_stats(df)

      user_stats(df)

      restart = input('\nWould you like to restart? Enter yes or no.\n')

      if restart.lower() != 'yes':

         break
      #print('Welcome')

   if __name__ == "__main__":

      main()
