"""Generated from Smithy shape ``com.amazonaws.shield#DescribeDRTAccessRequest``."""

from typing_extensions import TypedDict


class DescribeDRTAccessRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDRTAccessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDRTAccessRequest:
    out: DescribeDRTAccessRequest = {}  # type: ignore[typeddict-item]
    return out
