"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

NotebookInstanceSortOrder: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: NotebookInstanceSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookInstanceSortOrder value: {data!r}")
    return cast(NotebookInstanceSortOrder, data)
