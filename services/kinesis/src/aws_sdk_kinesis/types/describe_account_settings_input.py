"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeAccountSettingsInput``."""

from typing import TypedDict


class DescribeAccountSettingsInput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountSettingsInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountSettingsInput:
    out: DescribeAccountSettingsInput = {}  # type: ignore[typeddict-item]
    return out
