"""Generated from Smithy shape ``com.amazonaws.athena#DeleteNotebookOutput``."""

from typing_extensions import TypedDict


class DeleteNotebookOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNotebookOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNotebookOutput:
    out: DeleteNotebookOutput = {}  # type: ignore[typeddict-item]
    return out
