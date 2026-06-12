"""Generated from Smithy shape ``com.amazonaws.codebuild#SortOrderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

SortOrderType: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_aws_json_1_1(value: SortOrderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortOrderType value: {data!r}")
    return cast(SortOrderType, data)
