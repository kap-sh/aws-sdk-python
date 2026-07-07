"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StopLoggingResponse``."""

from typing_extensions import TypedDict


class StopLoggingResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopLoggingResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopLoggingResponse:
    out: StopLoggingResponse = {}  # type: ignore[typeddict-item]
    return out
