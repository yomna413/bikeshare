import time
import pandas as pd
import numpy as np
flag = True
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('***************Hello! Let\'s explore some US bikeshare data!***************\nplease enter which city you want:\n'
          'if you want chicago press a , if you want new york city b,if you want washington press c:')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities  = ['a' , 'b' , 'c']
    while 1:
        city = input().lower()
        if city in cities:
            break
        else:
            print('please enter a or b or c')


    months= ['all','january', 'february', 'march', 'april', 'may', 'june']
    # get user input for month (all, january, february, ... , june)

    while 1:
        print('which month you want : all, january, february, ... , june')
        month = input().lower()
        if month not in months:
            print ('please enter the month again')
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days =['all' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' , 'sunday']
    print('which day of the week you prefer  all , monday .. sunday?')
    while 1:
        day = input().lower()
        if day not in days:
            print('please enter the day again')
            continue
        else:
            break

    print("your data is city :{} , month:{}  , day: {}:".format(city, month, day))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (st to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if city == 'a':
        flag = True
        filename = 'chicago.csv'
    elif city == 'b':
        flag = True
        filename = 'new_york_city.csv'
    elif city == 'c':
        flag = False
        filename = 'washington.csv'




    df=pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of the week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day of the week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n***************Calculating The Most Frequent Times of Travel***************\n')
    start_time = time.time()

    # display the most common month
    c_m = df['month'].mode()[0]
    print("most popular month :", c_m)

    # display the most common day of week
    c_d = df['day of the week'].mode()[0]
    print("most popular day :", c_d)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("This took %s seconds.:" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n***************Calculating The Most Popular Stations and Trip***************\n')
    start_time = time.time()

    # display most commonly used start station
    start_st = df['Start Station'].mode()[0]
    print('most commonly station: \n', start_st)
    # display most commonly used end station

    end_st = df['End Station'].mode()[0]
    print('most commonly used end station: \n' , end_st)

    # display most frequent combination of start station and end station trip
    df['combinations'] = df['Start Station'] + df['End Station']
    m_c = df['combinations'].mode()[0]
    print ('most frequent combination of start:\n' , m_c )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n***************Calculating Trip Duration***************\n')
    start_time = time.time()

    # display total travel time
    t_t_t = df['Trip Duration'].sum()
    print('total travel time :\n' , t_t_t)
    # display mean travel time
    mean1 = df['Trip Duration'].mean
    print('mean of travel duration:\n', mean1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n***************Calculating User Stats***************\n')
    start_time = time.time()

    # Display counts of user types
    count = df['User Type'].count()
    print("User Types count:{}\n".format(count))

    # Display counts of gender
    if flag == True:
        gender_count = df['Gender'].count()
        print('gender counts :{}\n'.format(gender_count))
    else:
        print ("Gender stats cannot be calculated because Gender does not appear in the dataframe")

    # Display earliest, most recent, and most common year of birth
    earlist = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common = df['Birth Year'].mode()
    print(' Year of birth : earlist:{},\n most recent:{},\nmost common: {}\n'.format(earlist , most_recent, most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_display(df):
    print("\n***************Raw Display***************\n")
    start =0
    while 1:
        print ( 'do you want to see more 5 rows of data press yes else press no')
        inputy = input().lower()
        if (inputy == 'yes'):
            print(df.iloc[start:start+5])
            start+=5
        else :
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
