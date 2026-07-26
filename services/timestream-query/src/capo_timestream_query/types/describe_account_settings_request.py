"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeAccountSettingsRequest``."""

from typing_extensions import TypedDict


class DescribeAccountSettingsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAccountSettingsRequest:
    out: DescribeAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
