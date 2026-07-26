"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#AddApplicationOutputResponse``."""

from typing_extensions import TypedDict


class AddApplicationOutputResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationOutputResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationOutputResponse:
    out: AddApplicationOutputResponse = {}  # type: ignore[typeddict-item]
    return out
