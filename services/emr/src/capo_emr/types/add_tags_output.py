"""Generated from Smithy shape ``com.amazonaws.emr#AddTagsOutput``."""

from typing_extensions import TypedDict


class AddTagsOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsOutput:
    out: AddTagsOutput = {}  # type: ignore[typeddict-item]
    return out
