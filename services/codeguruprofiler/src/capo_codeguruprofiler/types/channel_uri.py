"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ChannelUri``."""

from typing import TypeAlias

"""Channel URI uniquely identifies a Notification Channel. TopicArn is the uri for an SNS channel, emailId is uri for an email channel etc. Currently we only support SNS channels and thus required to be an ARN"""
ChannelUri: TypeAlias = str
