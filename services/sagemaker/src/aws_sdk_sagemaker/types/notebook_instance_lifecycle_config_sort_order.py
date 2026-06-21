"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigSortOrder``."""

from typing import Literal, TypeAlias, cast

NotebookInstanceLifecycleConfigSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceLifecycleConfigSortOrder:
    return cast(NotebookInstanceLifecycleConfigSortOrder, data)
