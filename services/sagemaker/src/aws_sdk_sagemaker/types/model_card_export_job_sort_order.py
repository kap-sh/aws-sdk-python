"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardExportJobSortOrder: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ModelCardExportJobSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardExportJobSortOrder:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ModelCardExportJobSortOrder value: {data!r}"
        )
    return cast(ModelCardExportJobSortOrder, data)
