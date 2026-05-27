"""Generated from Smithy shape ``com.amazonaws.dynamodb#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long
    import aws_sdk_dynamodb.types.string


class Endpoint(TypedDict):
    address: "aws_sdk_dynamodb.types.string.String"
    """<p>IP address of the endpoint.</p>"""
    cache_period_in_minutes: "aws_sdk_dynamodb.types.long.Long"
    """<p>Endpoint cache time to live (TTL) value.</p>"""
