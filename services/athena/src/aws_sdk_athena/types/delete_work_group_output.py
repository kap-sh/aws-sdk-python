"""Generated from Smithy shape ``com.amazonaws.athena#DeleteWorkGroupOutput``."""

from typing_extensions import TypedDict


class DeleteWorkGroupOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkGroupOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkGroupOutput:
    out: DeleteWorkGroupOutput = {}  # type: ignore[typeddict-item]
    return out
