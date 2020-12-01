# Description

Create tickets in Jira for the top 25 most vulnerable assets scanned within the last 30 days.


# Key Features

* Find the 25 most vulnerable assets scanned within the last 30 days.
* Find solutions for the top 10 vulnerabilities on each asset
* Create a Jira ticket for each asset containing it's vulnerability solutions

# Requirements

* InsightVM
* Jira

# Documentation

## Setup

Import the workflow from the Rapid7 Extension Library and proceed through the Import Workflow wizard in InsightConnect. Import plugins, create or select connections, and rename the workflow as a part of the Import Workflow wizard as necessary.

Once the workflow has been imported, the Create Jira Ticket step will need to be configured. In the step the Project input will need to be changed from `change_me` to an appropriate project ID.

The frequency and time of at which the workflow runs my also be changed by editing the timer trigger. By default the workflow will run on the first day of the month at 12:01AM 

### Usage

*This workflow will only trigger in the channel specified in the Microsoft Teams workflow steps.*

To run the workflow, send a message to the specified Microsoft Teams channel starting with the command `!reset-password`. 

Commands should be in the following format:
`!reset-password john.doe@acme.inc`

## Technical Details

Plugins utilized by workflow:

|Plugin|Version|Count|
|----|----|--------|
|Jira|6.0.3|1|
|Python 3 Script|2.0.2|2|
|Timers|2.0.4|1|
|Rapid7 InsightVM|4.8.1|2|

## Troubleshooting

_There is no troubleshooting information at this time_

# Version History

* 1.0.0 - Initial workflow

# Links

## References

* [InsightVM](https://www.rapid7.com/products/insightvm/)
* [Jira](https://www.atlassian.com/software/jira)
