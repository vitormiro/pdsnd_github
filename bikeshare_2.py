import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

### def get_filters():
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter the city name (Chicago, New York City, Washington): \n').lower()
        if city.lower() in CITY_DATA.keys():
            print('You selected {}!'.format(city.title()))
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month (January, February, March, April, May, June, or all): \n')
        if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('You selected {}!'.format(month.title()))
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all):\n')
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print('You selected {}.'.format(day.title()))
            break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """

    df = pd.read_csv(CITY_DATA[city])

    """
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month: ' , common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common Day: ' , common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour: ' , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common End Station is:',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df['Start Station'] + "_" + df['End Station']
    trip_counts = frequent_combination.value_counts().idxmax()
    print('Most Frequent Combination of Start Station and End Station: ' , trip_counts)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average Travel Time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types: \n{}\n'.format(user_types))

    # TO DO: Display counts of gender
    # Considering missing columns in Washington data
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender count:\n{}\n'.format(gender))
    else:
        print('Gender data is not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    # Considering missing columns in Washington data
    if "Birth Year" in df.columns:
        birth_year = df['Birth Year']
        print('Earliest Year Of Birth:\n',df['Birth Year'].min())
        print('Most Recent Year Of Birth:\n',df['Birth Year'].max())
        print('Most Common Year Of Birth:\n',df['Birth Year'].mode()[0])
    else:
        print('Birth Year data is not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`
    """

    view_more = 'yes'
    while view_more == 'yes':
        for i in df.iterrows():
            count = 0
            while count < 5:
                print(i)
                count += 1
            reaction = input('\n Do you like to  display more data ? Yes or No?\n')
            if reaction.lower() == 'no':
                view_more = 'no'
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
