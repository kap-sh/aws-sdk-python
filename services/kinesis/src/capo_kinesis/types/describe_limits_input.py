"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeLimitsInput``."""

from typing_extensions import TypedDict


class DescribeLimitsInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLimitsInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLimitsInput:
    out: DescribeLimitsInput = {}  # type: ignore[typeddict-item]
    return out
