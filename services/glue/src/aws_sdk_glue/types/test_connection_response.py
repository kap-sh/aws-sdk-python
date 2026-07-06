"""Generated from Smithy shape ``com.amazonaws.glue#TestConnectionResponse``."""

from typing_extensions import TypedDict


class TestConnectionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionResponse:
    out: TestConnectionResponse = {}  # type: ignore[typeddict-item]
    return out
