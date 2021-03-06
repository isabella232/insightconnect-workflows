# Description

This workflow accepts a Microsoft Teams command containing an IP address. This IP address will be checked against a pre-defined address group in Fortinet to determine whether or not the IP address is present. It is assumed that this address group will be used to store IP addresses for a block policy. A message with the results will be returned.

Sample Microsoft Teams Trigger Commands:

`!block-status 198.51.100.100`
`!block-status example.com`

# Key Features

* The ability to see if an IP address is currently blocked by the firewall

# Requirements

* Microsoft Teams connection
* Admin API key to a Fortinet FortiGate firewall

# Documentation

## Setup

Import the workflow from the Rapid7 Extension Library and proceed through the Import Workflow wizard in InsightConnect. Import plugins, create or select connections, and rename the workflow as a part of the Import Workflow wizard as necessary.

In the _Check for IP Message_, _IP Blocked Message_, and _IP Not Blocked Message_ steps change the Team Name and Channel Name input from `change_me` to an appropriate team and channel.

In the _Check for IP_ step edit the Address Group Name input from `change_me` to an appropriate address group.

To run the workflow,  Use the command "!block-status <IP>". The workflow will post responses in the channel.

## Technical Details

Plugins utilized by workflow:

|Plugin|Version|Count|
|----|----|--------|
|Fortinet FortiGate|5.0.0|1|
|HTML|1.2.2|1|
|Microsoft Teams|2.2.1|4|

## Troubleshooting

_There is no troubleshooting information at this time_

# Version History

* 1.1.3 - Update Fortinet FortiGate, Microsoft Teams, and HTML plugins to latest versions
* 1.1.2 - Update Fortinet FortiGate and Microsoft Teams plugins to the latest versions | Added a new message if Fortinet FortiGate action fails
* 1.1.1 - Update to make Microsoft Teams plugin the latest version
* 1.1.0 - Update Fortinet FortiGate to latest version
* 1.0.0 - Initial workflow

# Links

## References

* [Fortinet](https://www.fortinet.com/)
* [Microsoft Teams](https://teams.microsoft.com)
