"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeEndpointsRequest``."""

from typing import TypedDict


class DescribeEndpointsRequest(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeEndpointsRequest:
    out: DescribeEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
