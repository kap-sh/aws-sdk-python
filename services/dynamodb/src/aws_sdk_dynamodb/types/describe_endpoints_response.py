"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.endpoints


class DescribeEndpointsResponse(TypedDict):
    endpoints: "aws_sdk_dynamodb.types.endpoints.Endpoints"
    """<p>List of endpoints.</p>"""
