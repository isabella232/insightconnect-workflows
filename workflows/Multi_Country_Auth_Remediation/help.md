# Description

This workflow triggers on InsightIDR MultiCountryAuthentication alerts and automatically deprovisions users if they are ingressing from non-whitelisted source IPs.

# Key Features

* Import a file or a string of whitelisted/VPN IPs
* Automatically correlate internal IPs with what IDR has detected
* Auto-suspend users on access from more than 1 whitelisted IP

# Requirements

# Documentation

## Setup

* Download the workflow or clone the repository `git clone https://github.com/rapid7/insightconnet-workflows.git`
* Login to InsightConnect, and “Import” the .icon file into the workflow builder
* Configure the connection for the AD/LDAP plugin
* Activate your workflow
* Navigate to IDR's alert triggers page at #/automation/alerts
* Click Create Alert Trigger
* Select Multi Country Auth Remediation
* While Selecting Alerts, check "Multi Country Authenticaiton"

## Technical Details

Plugins utilized by workflow:

|Plugin|Version|Count|
|----|----|--------|
|Python 3 Script|2.0.0|1|
|ExtractIt|1.1.6|1|
|Active Directory LDAP|3.2.4|1|

## Troubleshooting

_There is no troubleshooting information at this time_

# Version History

* 1.0.0 - Initial workflow

# Links

## Source Code

* https://github.com/rapid7/insightconnect-workflows/blob/master/workflows/Multi_Country_Auth_Remediation

## References

* https://github.com/rapid7/insightconnect-workflows