"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RemoveTagsFromResourceResponse``."""

from typing_extensions import TypedDict


class RemoveTagsFromResourceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceResponse:
    out: RemoveTagsFromResourceResponse = {}  # type: ignore[typeddict-item]
    return out
