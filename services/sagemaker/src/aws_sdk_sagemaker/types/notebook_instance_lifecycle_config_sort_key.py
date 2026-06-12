"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

NotebookInstanceLifecycleConfigSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "LastModifiedTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "LastModifiedTime",
    )
)


def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceLifecycleConfigSortKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NotebookInstanceLifecycleConfigSortKey value: {data!r}"
        )
    return cast(NotebookInstanceLifecycleConfigSortKey, data)
