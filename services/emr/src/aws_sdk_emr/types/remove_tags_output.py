"""Generated from Smithy shape ``com.amazonaws.emr#RemoveTagsOutput``."""

from typing_extensions import TypedDict


class RemoveTagsOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsOutput:
    out: RemoveTagsOutput = {}  # type: ignore[typeddict-item]
    return out
