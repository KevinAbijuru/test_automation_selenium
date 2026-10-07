from includes import functions
from includes import constants

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
    functions.test_click_item(constants.TEST_URL,test_url, test_name)

#Close the test activities after the test
print(f"End of test for all items. Closing the browser now...")
