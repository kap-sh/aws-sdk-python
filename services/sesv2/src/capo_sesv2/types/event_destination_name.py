"""Generated from Smithy shape ``com.amazonaws.sesv2#EventDestinationName``."""

from typing import TypeAlias

"""<p>The name of an event destination.</p> <p> <i>Events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.</p>"""
EventDestinationName: TypeAlias = str
