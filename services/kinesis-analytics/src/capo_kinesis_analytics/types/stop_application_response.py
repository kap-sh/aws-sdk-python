"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#StopApplicationResponse``."""

from typing_extensions import TypedDict


class StopApplicationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopApplicationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopApplicationResponse:
    out: StopApplicationResponse = {}  # type: ignore[typeddict-item]
    return out
