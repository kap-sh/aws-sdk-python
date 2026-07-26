"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeRegistryRequest``."""

from typing_extensions import TypedDict


class DescribeRegistryRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegistryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegistryRequest:
    out: DescribeRegistryRequest = {}  # type: ignore[typeddict-item]
    return out
