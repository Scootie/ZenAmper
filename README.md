
_Important Notice: This is a proof of concept script. I'm not responsible for the reprocussions of using this on your account. According to Hashtalk, auto amping is not allowed. Though from an enforcement perspective, it would be seriously hard to differentiate between this an a real user. Selenium uses a real browser, and is in essense recognized by the server as any another other real person using the selected browser. In fact, it's what web developers often use to test their own applications when simulating real users._

_Back on the enforcement bit, if you're double dipping in the same pool, in the way this script is currently setup for a Hashlet Prime mining HashPoint Pool, it probably will be a dead ringer for auto amping. A nonscripted version of this process would look like swapping out main mining pool from HashPoint to ZenPool then double dipping to HashPoint Pool and then swapping main pool to HashPoint Pool. Technically, the code base exists to choose a different pool than is currently being mined if you modify preference setting to a list remove currently mining pool from that list. Or another approach would be to use the DOM element to simulate the swapping in and out for the mainpool. Just random ideas from a thought experiment._

_FYI: This was never intended to be supported script, but I'll leave it in the repo who finds this python code helpful for their other projects. This script mostly provided me a decent opportunity to learn how to use Selenium and all its inner workings._ 

_From an error handling perspective, I'd say it's much more finky than Scrapy. Selenium is a good choice when you're scraping a webpage that loads a lot of stuff through javascript. As all of it is rendered in a real browser, handling the DOM is a much more fluid experience. However, the DOM loading, and transition between user actions like key inputs and clicking requires time offsets like sleep between commands so that you don't cause the script to process faster than the elements are available._

ZenAmper
========
Amping your Hashlet Prime is critical if you want to maintain ROI. The problem is that this requires manually logging into GAW's ZenPortal, and sometimes you're just not available to do so. Real-life gets in the way. This script solves that problem, and automatically amps your Primes in the way you want. 

## Notes about the script

This is not most efficient code in terms of length or performance. This was written with structure as perhaps the highest priority. Instead of directly calling webpage elements, we crawl the DOM to find nested values and elements. 

This allows us to correctly traverse the DOM, find the web element that represent each Hashlet Prime, sort which Hashlet Primes are available for amping, and then inspect deeper for controls. The benefit of this approach is that it's highly scaleable when there are multiple Hashlet Prime entries and the underlying code is more flexible when GAW makes changes to the web interface.

## Settings

Note that this script supports specific functionality. It will amp any available Hashlet Prime. However, it only has two adjustable settings: amp type and double dip pool. 

The zenamp_settings.py file contains the following:
```python
ZENMINER_USERNAME = 'username'
ZENMINER_PASSWORD = 'password'
PREFERENCE = 'Boost' #Options are 'DD' and 'Boost'
DD_ORDER = 'HashPoint Pool' #Other Options: 'ZenPool','CleverHashlet','HashletBit', 'LTC Pool', 'WaffleHashlet','MultiHashlet'
```

If you choose to double dip, it will only double dip a single pool for all hashlet primes. It cannot be set to double dip ZenPool for certain Primes and HashPoint Pool for others. 

As of 12/4/2014, GAW moved from a payouts at 8:00 AM PST to 00:00 AM PST. If you want to sync your amp payouts such that they do not overlap across days, please make adjustments accordingly with your own scheduled cron task.

## Optimizing Your ROI

Ideally you'll want to setup a cron job so this can be run frequently. Even though double dipping has a 12 hour amp time followed by a 12 hour cooldown, you could in theory run this every hour without any reprocussions. The log file will tell you when your Hashlet Primes have been successfully amped.

## Requirements
  
* Python bindings for Selenium
* Selenium server
 * JRE 1.6 or newer
  
## Installation instructions

Not provided.

## License

Copyright Caleb Ku 2014. Distributed under the MIT License. (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
