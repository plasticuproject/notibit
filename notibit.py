"""
    Main Application File
"""


from bitmain_connect import *
import time
import sys
import config

def get_text():

    # connect to bitmain website and grab html
    url = config.product
    response = simple_get(url)
    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')

    # find the value of the 'Sold Out/Add to cart' button
    button = soup.findAll('input', attrs = {'class' : 'btn-add m-t-20 btn-addCart'}, limit=None)
    buttonValue = button[0]['value']
    if buttonValue == 'Add to cart':  # run notify if button value is 'Add to cart'
        notify()


# main application loop
def main():
    running = True
    while running:
        try:
            time.sleep(120)  #reloads webpage every 2 minutes
            get_text()
        except KeyboardInterrupt:
            print(":  Interrupt received, stopping…")
            sys.exit()
        except UnboundLocalError:
            print("Connection Error")
            pass


if __name__ == "__main__":
    main()
