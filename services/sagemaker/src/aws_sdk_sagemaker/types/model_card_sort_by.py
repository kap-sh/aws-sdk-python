"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: ModelCardSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardSortBy value: {data!r}")
    return cast(ModelCardSortBy, data)
