"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceSortKey``."""

from typing import Literal, TypeAlias, cast

NotebookInstanceSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceSortKey:
    return cast(NotebookInstanceSortKey, data)
