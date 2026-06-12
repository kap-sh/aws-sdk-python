"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""Attribute by which to sort returned export jobs."""
ModelCardExportJobSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: ModelCardExportJobSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardExportJobSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardExportJobSortBy value: {data!r}")
    return cast(ModelCardExportJobSortBy, data)
