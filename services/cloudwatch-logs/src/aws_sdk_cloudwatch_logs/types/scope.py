"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Scope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

Scope: TypeAlias = Literal["ALL",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_aws_json_1_1(value: Scope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Scope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scope value: {data!r}")
    return cast(Scope, data)
