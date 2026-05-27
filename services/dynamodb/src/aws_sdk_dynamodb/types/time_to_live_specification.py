"""Generated from Smithy shape ``com.amazonaws.dynamodb#TimeToLiveSpecification``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_attribute_name
    import aws_sdk_dynamodb.types.time_to_live_enabled


class TimeToLiveSpecification(TypedDict):
    enabled: "aws_sdk_dynamodb.types.time_to_live_enabled.TimeToLiveEnabled"
    """<p>Indicates whether TTL is to be enabled (true) or disabled (false) on the table.</p>"""
    attribute_name: (
        "aws_sdk_dynamodb.types.time_to_live_attribute_name.TimeToLiveAttributeName"
    )
    """<p>The name of the TTL attribute used to store the expiration time for items in the table.</p>"""
