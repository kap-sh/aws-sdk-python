"""Generated from Smithy shape ``com.amazonaws.glue#DeleteDatabaseResponse``."""

from typing_extensions import TypedDict


class DeleteDatabaseResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatabaseResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatabaseResponse:
    out: DeleteDatabaseResponse = {}  # type: ignore[typeddict-item]
    return out
