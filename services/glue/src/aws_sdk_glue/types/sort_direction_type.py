"""Generated from Smithy shape ``com.amazonaws.glue#SortDirectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SortDirectionType: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DESCENDING",
        "ASCENDING",
    )
)


def serialize_aws_json_1_1(value: SortDirectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortDirectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortDirectionType value: {data!r}")
    return cast(SortDirectionType, data)
