"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeLimitsInput``."""

from typing import TypedDict


class DescribeLimitsInput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLimitsInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLimitsInput:
    out: DescribeLimitsInput = {}  # type: ignore[typeddict-item]
    return out
