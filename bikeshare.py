import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Would you like to see data for chicago, new york city, or washington? ")
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Invalid city, please try again")
            continue
        else:
            break
   
    while True:
        month = input("Would you like to filter by month? If yes type january, february, march, april, may, or june, if not type all instead: ")
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Invalid month, please try again")
            continue
        else:
            break


    while True:
        day = input("Would you like to filter by day? If yes type monday, tuesday, wednesday, thursday, friday, saurday or sunday, if not type all instead: ")
        day = day.lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("Invalid day, please try again")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_name'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\n The Most common month is ',df['month'].value_counts().idxmax())

    print('\n The Most common day is ',df['day_name'].value_counts().idxmax())

    df['hour'] = df['Start Time'].dt.hour
    print('\n The Most common hour is ',df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('\n The Most commonly used start station is ', df['Start Station'].value_counts().idxmax())

    print('\n The Most commonly used end station is ', df['End Station'].value_counts().idxmax())

    df['combination'] = df['Start Station'] + " " + df['End Station']
    print('\n The Most frequent combination of start station and end station trip is ',df['combination'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time  = df['Trip Duration'].sum() / 3600.0
    print('\nTotal travel time = ', total_time)

    mean_time  = df['Trip Duration'].mean() / 3600.0
    print('\nTotal travel time = ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('Count of user types = ',user_types)
    
    try:
        gender = df['Gender'].value_counts()
        print('Count of gender = ',gender)
    except KeyError:
        print("Gender data is not available for this city.")
    

    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].value_counts().idxmax())
        print('\nEarliest year of birth = ',earliest)
        print('\nMost recent year of birth = ',most_recent)
        print('\nMost common year of birth = ',most_common)
    except KeyError:
        print("\nBirth year data is not available for this city.")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    lines = 1
    while True:
        data = input("\nWould you like to see 5 lines of raw data? type yes or no: ")
        data = data.lower()
        
        if data == 'yes':
            print(df[lines:lines+5])
            lines = lines + 5 
        elif data == 'no':
            break
        else:
            print("\nInvalid input, please type yes or no.")
            
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
        if restart.lower() == 'no':
            break
        
        elif restart.lower() == 'yes':
            continue

        else:
            print("\nInvalid input, please enter yes or no.")


if __name__ == "__main__":
	main()