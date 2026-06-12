"""Generated from Smithy shape ``com.amazonaws.glue#Sort``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

Sort: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_aws_json_1_1(value: Sort) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Sort:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Sort value: {data!r}")
    return cast(Sort, data)
