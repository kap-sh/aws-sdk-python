"""Generated from Smithy shape ``com.amazonaws.athena#CreateWorkGroupOutput``."""

from typing_extensions import TypedDict


class CreateWorkGroupOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkGroupOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkGroupOutput:
    out: CreateWorkGroupOutput = {}  # type: ignore[typeddict-item]
    return out
