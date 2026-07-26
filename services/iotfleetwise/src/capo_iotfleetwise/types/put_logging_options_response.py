"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PutLoggingOptionsResponse``."""

from typing_extensions import TypedDict


class PutLoggingOptionsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutLoggingOptionsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> PutLoggingOptionsResponse:
    out: PutLoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    return out
