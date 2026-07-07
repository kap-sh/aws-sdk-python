"""Generated from Smithy shape ``com.amazonaws.glue#DeleteConnectionTypeResponse``."""

from typing_extensions import TypedDict


class DeleteConnectionTypeResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionTypeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionTypeResponse:
    out: DeleteConnectionTypeResponse = {}  # type: ignore[typeddict-item]
    return out
