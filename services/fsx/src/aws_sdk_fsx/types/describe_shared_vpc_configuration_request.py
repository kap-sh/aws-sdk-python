"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeSharedVpcConfigurationRequest``."""

from typing_extensions import TypedDict


class DescribeSharedVpcConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSharedVpcConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSharedVpcConfigurationRequest:
    out: DescribeSharedVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
