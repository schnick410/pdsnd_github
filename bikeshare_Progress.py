import time
import pandas as pd
import numpy as np

#TODO: Define dict for importing the correct data based on user input later on
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""List for inputs for month"""

MONTH_DATA = [0, 1, 2, 3, 4, 5, 6]

# TODO: Define month grouping, so that entered integer can be converted into a text
MONTH_GROUPING = {0: 'no selection', 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}

"""List for input for days (Monday = 0)"""

DAY_DATA = [0, 1, 2, 3, 4, 5, 6, 7]

""" List to group day number to day name """

# TODO: Define day grouping, so that entered integer can be converted into a text
DAY_GROUPING = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday', 7: 'no selection'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TODO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city= str(input('Which city are you interested in today? ')).lower()
    print()

    # TODO: get user input for month (all, january, february, ... , june)

    while city not in CITY_DATA.keys():
        city = str(input('That is not a valid input. You can select between Chicaco, New York City and Washington. Please enter again: - ')).lower()
    print('you selected the following city: ', city, '\n')
    #insert empty space for higher user convenience while using
    print(MONTH_GROUPING)

    month = int(input('\nWhich month would you like to select? Please provide a NUMBER of the above mentioned months.\n'))

    while month not in MONTH_DATA:
        month = int(input(' That is not a valid input. You can select between the NUMBERS 1-6 or you can type 0 for no selection as shown above: - '))
    print('Great, you choose the following month number {}, which equals {}.\n'.format(month, MONTH_GROUPING[month]))
    #insert empty space for higher user convenience while using

    print(DAY_GROUPING, "\n" )
    day = int(input('Which day would you like to see? Select from the above shown day numbers - '))

    while day not in DAY_DATA:
        day = int(input('That is not a valid input. Please choose a number between 1 and 7 for the day selection. You can also choose 0, if you do not want to filter for a day.\n'))
    print('Good choice! You selected the following day number {}, which equals {}.\n'.format(day, DAY_GROUPING[day]))

    print('-'*40)
    return city, month, day


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
    #importing the data for the City
    df = pd.read_csv(CITY_DATA[city])
    # extract hour, weekday and month from Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['weekday'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Todo: display the most common month

    if month == 0:
        mc_month = df['month'].mode()[0]
        print(' The month with the highest use of bike sharing is: ', mc_month)

    # TODO: display the most common day of week

    if day == 7:
        mc_day = df['weekday'].mode()[0]
        print(' The day with the highest use of bike sharing is: ', mc_day)

    # TODO: display the most common start hour
    mc_hour = df['hour'].mode()[0]
    print(' The hour with the highest use of bike sharing is: ', mc_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TODO: display most commonly used start station
    mc_start = df['Start Station'].mode()[0]
    print('\nThe most used Start Station is: ', mc_start)

    # TODO: display most commonly used end station
    mc_end = df['End Station'].mode()[0]
    print('\nThe most used End Station is: ', mc_end)

    # TODO: display most frequent combination of start station and end station trip

    df['Start - End'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    mc_start_to_end = df['Start - End'].mode()[0]
    print('\nThe most frequently used drive is ', mc_start_to_end, '.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TODO: Calculate total trip Duration
    #Total trip duration is displayed in hours and shown with no decimal.

    td_total_minutes = df['Trip Duration'].sum()
    td_total_hours = int(round(td_total_minutes / 60 / 60, 0))

    if month != 0 and day != 7:
        print(('\nThe total trip duration on day {} in month {} is {} hours.').format(day, month, td_total_hours))
    elif month == 0 and day == 7:
        print(('\nThe total trip duration is {} hours.').format(td_total_hours))
    elif month == 0:
        print(('The total trip duration on day {} over all months is {} hours.').format(day, td_total_hours))
    elif day == 7:
        print(('\nThe total trip duration over the total month number {} is {} hours.').format(month, td_total_hours))

    # TODO: Calculate the average trip Duration
    # Average Trip duration is rounded to the nearest full minute

    avg_td_minutes = int(round(df['Trip Duration'].mean() /60, 0))
    print(('\nThe average travel time for the given specifications is {} minutes.').format(avg_td_minutes))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TODO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print(count_user_type)

    # Display counts of gender; Washington has no column for gender, if washington is selected, nothing should be shown
    if city != 'washington':
        count_gender = df['Gender'].value_counts()
        print (count_gender)


    # TODO: Display earliest, most recent, and most common year of birth, again there is no birth year in washington

    # Earliest year of birth equals the minimum of the numbers in birth year, highest equals max, most common equals mode[0]
    if city != 'washington':
        earliest_birth_year = int(df['Birth Year'].min())
        print ('The youngest user was born in:', earliest_birth_year)
        highest_birth_year = int(df['Birth Year'].max())
        print ('The oldest user was born in:', highest_birth_year)
        mc_birth_year = int(df['Birth Year'].mode()[0])
        print ('The most common birth year was:', mc_birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df, month, day)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
