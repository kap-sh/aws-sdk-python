"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookOutputOption``."""

from typing import Literal, TypeAlias, cast

NotebookOutputOption: TypeAlias = Literal[
    "Allowed",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookOutputOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookOutputOption:
    return cast(NotebookOutputOption, data)
