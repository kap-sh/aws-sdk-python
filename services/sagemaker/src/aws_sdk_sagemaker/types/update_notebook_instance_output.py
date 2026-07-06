"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateNotebookInstanceOutput``."""

from typing_extensions import TypedDict


class UpdateNotebookInstanceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotebookInstanceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotebookInstanceOutput:
    out: UpdateNotebookInstanceOutput = {}  # type: ignore[typeddict-item]
    return out
