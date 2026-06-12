"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

NotebookInstanceLifecycleConfigSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceLifecycleConfigSortOrder:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NotebookInstanceLifecycleConfigSortOrder value: {data!r}"
        )
    return cast(NotebookInstanceLifecycleConfigSortOrder, data)
