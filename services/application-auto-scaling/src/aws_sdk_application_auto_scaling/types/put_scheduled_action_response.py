"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PutScheduledActionResponse``."""

from typing_extensions import TypedDict


class PutScheduledActionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutScheduledActionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutScheduledActionResponse:
    out: PutScheduledActionResponse = {}  # type: ignore[typeddict-item]
    return out
