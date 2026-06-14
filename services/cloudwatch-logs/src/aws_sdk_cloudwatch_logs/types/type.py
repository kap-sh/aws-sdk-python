"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

Type: TypeAlias = Literal[
    "boolean",
    "integer",
    "double",
    "string",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "boolean",
        "integer",
        "double",
        "string",
    )
)


def serialize_aws_json_1_1(value: Type) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
