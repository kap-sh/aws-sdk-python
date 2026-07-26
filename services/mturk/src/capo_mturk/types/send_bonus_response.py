"""Generated from Smithy shape ``com.amazonaws.mturk#SendBonusResponse``."""

from typing_extensions import TypedDict


class SendBonusResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendBonusResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> SendBonusResponse:
    out: SendBonusResponse = {}  # type: ignore[typeddict-item]
    return out
