"""Generated from Smithy shape ``com.amazonaws.wafv2#LogScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

LogScope: TypeAlias = Literal[
    "CUSTOMER",
    "SECURITY_LAKE",
    "CLOUDWATCH_TELEMETRY_RULE_MANAGED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "SECURITY_LAKE",
        "CLOUDWATCH_TELEMETRY_RULE_MANAGED",
    )
)


def serialize_aws_json_1_1(value: LogScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogScope value: {data!r}")
    return cast(LogScope, data)
