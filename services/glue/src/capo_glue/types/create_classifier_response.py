"""Generated from Smithy shape ``com.amazonaws.glue#CreateClassifierResponse``."""

from typing_extensions import TypedDict


class CreateClassifierResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClassifierResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClassifierResponse:
    out: CreateClassifierResponse = {}  # type: ignore[typeddict-item]
    return out
