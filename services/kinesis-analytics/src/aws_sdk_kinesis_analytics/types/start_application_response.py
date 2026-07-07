"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#StartApplicationResponse``."""

from typing_extensions import TypedDict


class StartApplicationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartApplicationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartApplicationResponse:
    out: StartApplicationResponse = {}  # type: ignore[typeddict-item]
    return out
