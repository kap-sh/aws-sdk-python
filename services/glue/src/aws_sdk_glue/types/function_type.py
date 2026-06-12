"""Generated from Smithy shape ``com.amazonaws.glue#FunctionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FunctionType: TypeAlias = Literal[
    "REGULAR_FUNCTION",
    "AGGREGATE_FUNCTION",
    "STORED_PROCEDURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGULAR_FUNCTION",
        "AGGREGATE_FUNCTION",
        "STORED_PROCEDURE",
    )
)


def serialize_aws_json_1_1(value: FunctionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FunctionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FunctionType value: {data!r}")
    return cast(FunctionType, data)
