"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigSortKey``."""

from typing import Literal, TypeAlias, cast

NotebookInstanceLifecycleConfigSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "LastModifiedTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceLifecycleConfigSortKey:
    return cast(NotebookInstanceLifecycleConfigSortKey, data)
