"""Generated from Smithy shape ``com.amazonaws.glue#CreateDatabaseResponse``."""

from typing_extensions import TypedDict


class CreateDatabaseResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatabaseResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatabaseResponse:
    out: CreateDatabaseResponse = {}  # type: ignore[typeddict-item]
    return out
