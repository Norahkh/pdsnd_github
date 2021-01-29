import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_input(input_str,input_type):
    """ check input to keep asking users when they enter invalid inputs"""
    # use loop to keep running the question
    while True:
        input_read=input(input_str).lower()
        # detect when the user enters data that can't be process
        try:
            if input_read in ('chicago','new york city','washington') and input_type==1:
                break
            elif input_read in ('january','february','march','april','may','june','all') and input_type==2:
                break
            elif input_read in ('sunday','monday','tuesday','wednsday','thursday','friday','saturday','all') and input_type==3:
                break
            else:
                if input_type==1:
                    print('your input should be one of chicago, new york city or washington')
                if input_type==2:
                    print('your input should be one of the first six months')
                if input_type==3:
                    print('your input should be a day')
        except ValueError:
            print('sorry Error input')
    return input_read

def get_filters():
    """ get filters to ask user input for city, month and day """
    print('Hello! Let\'s explore some US bikeshare data!')
    # ask the user to write input for city, month and day
    # and give every function input type to verify if the user input is valid
    city = check_input('\nWhich city of chicago, new york city or washington you would like to choose?\n',1)
    month = check_input('\nWhich month you would like to see?\n',2)
    day = check_input('\nwhich day you would like to see?\n',3)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print(df['month'].mode()[0])
    # TO DO: display the most common day of week
    print(df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print(df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    group_field =df.groupby(['Start Station','End Station'])
    print(group_field.size().sort_values(ascending=False).head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    if city != 'washington':
    # TO DO: Display counts of gender
        print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print(df['Birth Year'].mode()[0])
        print(df['Birth Year'].max())
        print(df['Birth Year'].min())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Ask users if they want display raw data and print 5 raw
    raw = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('\nDo you want to see more of raw data? Enter yes or no\n')
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
