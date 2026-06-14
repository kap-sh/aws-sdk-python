"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PolicyScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

PolicyScope: TypeAlias = Literal[
    "ACCOUNT",
    "RESOURCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "RESOURCE",
    )
)


def serialize_aws_json_1_1(value: PolicyScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyScope value: {data!r}")
    return cast(PolicyScope, data)
