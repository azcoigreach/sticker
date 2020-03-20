#!/usr/bin/env python
import threading
import click
import coloredlogs, logging
import pickle
import signal
import time
import scrollphathd
from scrollphathd.fonts import font3x5
import pandas as pd
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')

@click.command()
@click.option('--memo', default=' Sticker:')
@click.option('--input', default='/home/pi/sticker/sticker.pickle')
@click.option('--duration', default=0.1, help='Refresh duration - 0.05s')
def sticker(memo,input,duration):
    '''Sticker Scroller by AZcoigreach'''
    try:
        click.clear()
        click.secho('Sticker Scroll Running...', fg='red')
        scrollphathd.rotate(degrees=180)
        tmp = str('')
        msg = ' .'
        scrollphathd.write_string(str(msg), font=font3x5, brightness=0.15)
        while True:
            data = pd.DataFrame(pickle.load(open(input, 'rb')))
            datatest = str(data)
            logging.debug('data DataFrame: %s', datatest)
            logging.debug('tmp DataFrame: %s', tmp)
            if datatest != tmp:
                logging.info('Updating DataFrame...')
                tmp = str(data)
                data = data.tail(1)
                data = data.iloc[0,3]
                msg = memo + str(data)
                scrollphathd.clear()
                scrollphathd.write_string(str(msg), font=font3x5, brightness=0.15)
                click.secho(msg, fg='yellow')
            logging.debug('Updating LED...')
            scrollphathd.show()
            scrollphathd.scroll()
            time.sleep(duration)
    except Exception as err:
        logger.error('Scroll Error: %s', err)
        time.sleep(5)
        sticker()
        

if __name__ == '__main__':
    sticker()