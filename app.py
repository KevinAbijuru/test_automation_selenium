from includes import functions
from includes import constants
from datetime import datetime

#Create an array of the texts and URLs as well so that they are looped through in the test.
text_url_array = {
    constants.ABOUT_TEXT: constants.ABOUT_URL,
    constants.PORTFOLIO_TEXT: constants.PORTFOLIO_URL,
    constants.SERVICES_TEXT: constants.SERVICES_URL,
    constants.CONTACT_TEXT: constants.CONTACT_URL,
    constants.HOME_TEXT: constants.HOME_URL 
}

#Try and loop through an array 
for test_name, test_url in text_url_array.items():
    #Call the function that it to perform the actual test
    test_results = functions.test_click_item(constants.TEST_URL,test_url, test_name)
    print(f"All tests have been completed. Please check the log file for details. {test_results}")

    #Create a log file to hold the test results. The log file will be created in the logs directory with a timestamp in the filename.
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    lines_of_text = [
        f"Test Title:{test_name}\n",
        f"Test URL:{test_url}\n",
        f"Target URL:{text_url_array}\n",
        f"Result:{test_results}\n"
        f"Time of test:{now}\n",
        f"----------------------------------------\n"
    ]

    #Write the lines of text to a log file
    with open(f"logs/LOG_FILE_{timestamp}.txt", "w", encoding="utf-8") as file:
        file.writelines(lines_of_text)

# Close the browser after all tests.
functions.close_browser()
print("End of test for all items. Closing the browser now...")
