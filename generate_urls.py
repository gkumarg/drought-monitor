import datetime

# Define start and end dates
start_date = datetime.date(2003, 3, 1)
end_date = datetime.date(2023, 3, 1)

# Define the URL format string

# Drought map
url_template = 'https://droughtmonitor.unl.edu/data/png/{date}/{date}_west_trd.png'

# 24 hour precipitation areas and amounts map (use create_video_gifs.py for this)
# http://www.wpc.ncep.noaa.gov/dailywxmap/dwm_prcn_20221229.html
# url_template = 'http://www.wpc.ncep.noaa.gov/dailywxmap/htmlimages/precip_{date}.gif'


# Define the output file name
output_file = 'urls.txt'

# Open the file for writing
with open(output_file, 'w') as f:
    # Loop over dates in 7-day increments
    delta = datetime.timedelta(days=30)
    d = start_date
    while d <= end_date:
        # Format the URL for the current date
        url = url_template.format(date=d.strftime('%Y%m%d'))
        # Write the URL to the file
        f.write(url + '\n')
        # Increment the date
        d += delta

print("Done")