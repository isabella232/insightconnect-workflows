# Description

This workflow accepts a Microsoft Teams command containing an IP address. The IP address will be put into or removed from an address group in Fortinet with a block policy.
A message with the results will be returned in the Microsoft Teams channel.

Sample Microsoft Teams Trigger Commands:

`!block-host 198.51.100.100`

`!unblock-host 198.51.100.100/15`

# Key Features

* Block an IP address
* Unblock an IP address

# Requirements

* Microsoft Teams connection
* Admin API key to a Fortinet FortiGate firewall

# Documentation

## Setup

Import the workflow from the Rapid7 Extension Library and proceed through the Import Workflow wizard in InsightConnect. Import plugins, create or select connections, and rename the workflow as a part of the Import Workflow wizard as necessary.

In the following steps, update the Team Name and Channel Name input from `change_me` to an appropriate team and channel:
* _Workflow Trigger_
* _Print IP Blocked Message_
* _Print Failed to Block IP Message_
* _Print No Action Taken Message_
* _Print Host is not on a Block List Message_
* _Print IP Unblocked Message_
* _Print IP Still Blocked Message_

Create an Address Group in Fortinet Firewall with the block policy enabled.

In the following steps edit the Address Group Name input from `change_me` to the Address Group Name.
* _Block IP in the Firewall_
* _Check for the IP in the Firewall_
* _Unblock the IP in the Firewall_

To run the workflow, use the command in the Microsoft Teams Channel selected Setup. The workflow will post responses in the channel.

## Technical Details

Plugins utilized by workflow:

|Plugin|Version|Count|
|----|----|--------|
|Fortinet FortiGate|1.1.0|3|
|HTML|1.2.1|1|
|Microsoft Teams|2.0.2|7|
|Python 3 Script|2.0.1|1|

## Troubleshooting

_There is no troubleshooting information at this time_

# Version History

* 1.0.0 - Initial workflow

# Links

## References

* [Fortinet](https://www.fortinet.com/)
* [Microsoft Teams](https://teams.microsoft.com)
