import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = { 'january': 1,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6,'jan': 1,'feb': 2,'mar': 3,'apr': 4,'may': 5,'jun': 6}

WEEK_DATA = { 'monday': 0,'tuesday': 1,'wednesday': 2,'thursday': 3,'friday': 4,'saturday': 5,'sunday': 6,'mon': 0,'tues': 1,'wed': 2,'thur': 3,'fri': 4,'sat': 5,'sun': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello \n \n Let\'s explore some of Divy Co. bikeshare system data, please follow the input requiremnts carefully to insure accurate results')
    print()
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        print('Pleasae select the city you want to look for')
        city = input('Chicago/CH, New York/NY, or Washington/WA? ').lower()
        print()
        if city=='ch':
            city='chicago'
        if city=='ny':
            city='new york city'
        if city=='wa':
            city='washington'
        if city not in CITY_DATA:
            print('The city you\'ve choose is non applicable, please choose a valid city')
            continue
        city = CITY_DATA[city]
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        choice = input('Do you want to filter the data by month and/or week? Yes/No ').lower()
        print()
        if choice=='yes':
            choice=True
        elif choice=='no':
            choice=False
        else:
            print('You did not enter a valid choice. Let\'s try again. ')
            continue
        break

    while 1:
        if choice:
            filter=input('You can filter by month / day / both ').lower()
            print()
            if filter=='month':
                print('Which month\'s data to look at?')
                month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun- ').lower()
                print()
                if month not in MONTH_DATA:
                    print('The month you choose is not applicable, please try again')
                    continue
                month = MONTH_DATA[month]
                day='all'
            elif filter=='day':
                print('Which day\'s data to look at? ')
                day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun- ').lower()
                print()
                if day not in WEEK_DATA:
                    print('The day you choose is not applicable, please try again')
                    continue
                day = WEEK_DATA[day]
                month='all'
            elif filter=='both':
                print('Which month\'s data to look at?')
                month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun- ').lower()
                print()
                if month not in MONTH_DATA:
                    print('The input is incorrect, please try again')
                    continue
                month = MONTH_DATA[month]
                print('please seclect the day of the week?')
                day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun- ').lower()
                print()
                if day not in WEEK_DATA:
                    print('The input is incorrect, please try again')
                    continue
                day = WEEK_DATA[day]
            else:
                print('The input is incorrect, please try again')
                continue
            break
        else:
            day='all'
            month='all'
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "no" to apply no month filter
        (str) day - name of the day of week to filter by, or "no" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if day != 'all':
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    #display the most common month
    most_freq_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==most_freq_month:
            most_freq_month = num.title()
    print('The most common month for travel is {}'.format(most_freq_month))

    #display the most common day of week
    most_freq_day = df['day_of_week'].mode()[0]
    for num in WEEK_DATA:
        if WEEK_DATA[num]==most_freq_day:
            most_freq_day = num.title()
    print('The most common day of week for travel is {}'.format(most_freq_day))

    #display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_freq_hour = df['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(most_freq_hour))
    df.drop('hour',axis=1,inplace=True)
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    start_stations_count = df['Start Station'].value_counts()
    print('Most Common Start Station :{} , count: {} '.format(popular_start_station , start_stations_count[popular_start_station]))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    end_stations_count = df['End Station'].value_counts()
    print('Most Common End Station :{} , count: {} '.format(popular_end_station , end_stations_count[popular_end_station]))


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] ='Start: '+ df['Start Station'] +' , ' +'End: '+ df['End Station']
    popular_trip = df['Trip'].mode()[0]
    trip_count = df['Trip'].value_counts()
    print('Most Common Trip :({}) , count:{} '.format(popular_trip , trip_count[popular_trip]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_durations = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    #display total travel time
    print()
    td_sum = df['Trip Duration'].sum()
    sum_seconds = td_sum%60
    sum_minutes = td_sum//60%60
    sum_hours = td_sum//3600%60
    sum_days = td_sum//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    #display mean travel time
    print()
    td_mean = math.ceil(df['Trip Duration'].mean())
    mean_seconds = td_mean%60
    mean_minutes = td_mean//60%60
    mean_hours = td_mean//3600%60
    mean_days = td_mean//24//3600
    print('Passengers travelled an average of {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_data(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Count of each user type : \n{}'.format(user_types_count))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('no gender data for this city')
    else:
        gender_of_users = df.groupby('Gender',as_index=False).count()
        print('Number of genders of users mentioned in the data are {}'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s - {}'.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Data related to birth year of users is not available for this city.')
    else:
        print("The earliest birth year is: {}".format(
                str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: {}".format(
                str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    end_loc = 5

    choice = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if choice=='yes':
        choice=True
    elif choice=='no':
        choice=False
    else:
        print('You did not enter a valid choice. Let\'s try that again. ')
        display_data(df)
        return

    if choice:
        while 1:
            end_loc <= df.shape[0] - 1

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            choice = input('Another five? Yes/No ').lower()
            if choice=='yes':
                continue
            elif choice=='no':
                break
            else:
                print('You did not enter a valid choice.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_data(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart == 'yes':
            continue
        elif restart=='no':
            break
        else:
            print('You did not enter a valid choice. Please rerun the program')
            return

if __name__ == "__main__":
	main()
