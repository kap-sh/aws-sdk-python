"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#QueueId``."""

from typing import TypeAlias

"""The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number."""
QueueId: TypeAlias = str
