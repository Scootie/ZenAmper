ZenAmper
========
Amping your Hashlet Prime is critical if you want to maintain ROI. The problem is that this requires manually logging into GAW's ZenPortal, and sometimes you're just not available to do so. Real-life gets in the way. This script solves that problem, and automatically amps your Primes in the way you want. 

## Notes about the script

This is not most efficient code in terms of length or performance. This was written with structure as perhaps the highest priority. Instead of directly calling webpage elements, we crawl the DOM to find nested values and elements. 

This allows us to correctly parse the web elements that represent each Hashlet Prime, sort which Hashlet Primes are available for amping, and then inspect deeper for controls. The benefit of this approach is that it's highly scaleable when there are multiple Hashlet Prime entries and the underlying code is more flexible when GAW makes chances to the web interface.

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

See included installation file for how to setup Selenium to use this script.

## License

Copyright Caleb Ku 2014. Distributed under the MIT License. (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
