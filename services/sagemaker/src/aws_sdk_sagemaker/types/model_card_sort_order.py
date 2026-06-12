"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardSortOrder: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ModelCardSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardSortOrder value: {data!r}")
    return cast(ModelCardSortOrder, data)
