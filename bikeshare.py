import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA=['all','jan' ,'feb','mar' ,'apr' ,'may' ,'june']
DAY_DATA=['all','saturday' , 'sunday', 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday']

   
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    """
    First i used def function to make loops to shortcut my codes and running repeatly
    """
        
    print('Hello! Let\'s explore some US bikeshare data!')

    '''tell the user to chooe between 3 diff. cities , 6 diff. months(or all) and diff 7 days(or all)  '''
    '''here i used while loops to let the user know his mistake in typing to type the correct data'''
    
    city=input('Kindly select a city from this cities( chicago , new york city and washington ): ').lower()
    while city not in CITY_DATA.keys() :
        print('There is no such a city name')
        city=input('Kindly select a city from this cities( chicago , new york city and washington ): ').lower()

    month=input('please,write a month name or all as following: all ,jan ,feb ,mar ,apr ,may or june: ' ).lower()
    while month not in MONTH_DATA :
        print('There is no such a month')
        month=input('please,write a month name or all as following: all ,jan ,feb ,mar ,apr ,may or june: ' ).lower()

    day=input('please, write a day name or all as following: all ,saturday , sunday , monday , tuesday , wednesday , thursday or friday: ').lower()
    while day not in DAY_DATA :
        print('There is no such a day')
        day=input('please, write a day name or all as following: all ,saturday , sunday , monday , tuesday , wednesday , thursday or friday: ').lower()

    print('-'*40)
    return city,month,day


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

    ''' Got from csv.files the data i want and made a new columns to separate specific data'''
    '''here i used read method to read csv file and get data from it like gender ,start time and start station and so on '''
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.strftime("%A")
    '''used if loop to make the user type the right month and day that he/she want to display and even all data too'''
    if month != 'all':
        months=['jan','feb','mar','apr','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]



    if day != 'all':

        df=df[df['day_of_week']== day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    '''To got a detailed info about common month,day and hour'''
    '''what if user need to know the month , day or hour that people uses the bikes alot..here's the code to help him/her'''
    
    most_common_month=df['month'].mode()[0]

    most_common_day=df['day_of_week'].mode()[0]

    df['hour']=df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('Most Common Month :',most_common_month)
    print('Most Common Day :',most_common_day)
    print('Most Common Hour :',most_common_hour)
    print('-'*40)

    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    ''' This is how we got to know the most starting station and the end too,and frequent comb. betwwen start and end station'''
    
    common_start_station=(df['Start Station']).mode()[0]

    common_end_station=df['End Station'].mode()[0]

    freq_comb=(df['Start Station']+'&'+df['End Station']).value_counts().head()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('common start station: ',common_start_station)
    print('common end station: ',common_end_station)
    print('freq comb: ',freq_comb)
    print('-'*40)
    return(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    '''Showing the total travel time that happened in specific data that the user needed and the mean too'''
    
    total_travel_time=df['Trip Duration'].sum()

    mean_travel_time=df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('Total Travel Duration : ',total_travel_time)
    print('Mean Travel Time : ',mean_travel_time)
    print('-'*40)
    return df


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    '''How many types that used those bike that day?.this is how we know this,
    also how many males and females and what the year of birth for the most people who uses this service'''

    count_user_types=df['User Type'].value_counts()


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('Count of user types : ',count_user_types)
    
    '''some data that's in csv files dosen't contain some informations...that's why i used if loop to not break my code and make errors'''
    
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print('no data available')


    if 'Birth Year' in df:
        print(df['Birth Year'].mode()[0].max())
    else:
        print('no data available')

    '''what if the user needs more info about trips..here's the code i used to display 5 rows of informations..i think that's helps the user'''
        
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no :\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[ start_loc : (start_loc +5)])
        start_loc+=5
        view_display = input('Do you wish to continue?: ').lower()

    
        if view_display != 'yes':
            break
    '''sometimes users got the info they need..so i used if loop to ask the user if he's okay or need more informations'''



    print('-'*40)
    return df

    '''this def code that runs all the above'''
    
def main():
    
    
    
    while True:
        city, month, day= get_filters()
        df=load_data(city,month,day)
        print(df.head())
        print(station_stats(df))
        print(time_stats(df))
        print(trip_duration_stats(df))
        print(user_stats(df))

    
        restart=input('would you like to restart? yes or no:  ')
        if restart.lower() != 'yes':
            break
        '''need to change the city,month or day..no problem here's code to repeat the all process'''

if __name__ == "__main__":
    main()
