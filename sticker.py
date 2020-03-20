import time
import yfinance as yf
import click
import coloredlogs, logging
import pickle
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')

@click.command()
@click.option('--symbol', default='^DJI', help='example: ^DJI MSFT AAPL')
@click.option('--period', default='1d', help='valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max')
@click.option('--start', default=None, help='yyyy-mm-dd')
@click.option('--end', default=None, help='yyyy-mm-dd')
@click.option('--output', default='/home/pi/sticker/sticker.pickle', help='/home/pi/sticker/sticker.pickle')
@click.option('--duration', default=30, help='Refresh duration - default 5 mins')
def sticker(symbol,period,start,end,output,duration):
    """STicker by AZcoigrech
    Report Stock information to pickle for use in other applications"""
    try:
        while True:
            click.clear()
            click.secho('STicker Executing', fg='red', bold=True)
            click.secho(str('Symbol:'+str(symbol)+' Period:'+str(period)+' Start:'+str(start)+' End:'+str(end)), fg='yellow')
            tickerData = yf.Ticker(symbol)
            tickerDf = tickerData.history(period=period, start=start, end=end)
            if output is not None:
                click.secho(str('Output:'+output), fg='blue')
                pickle.dump(tickerDf, open(output, 'wb'))
            click.secho(str(tickerDf), bg='green', fg='black')
            time.sleep(duration)
                    
    except Exception as err:
        logger.error('STicker Error: %s', err)
if __name__ == '__main__':
    sticker()