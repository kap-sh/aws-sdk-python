"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetProxyRuleType: TypeAlias = Literal[
    "DOMAIN",
    "IP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOMAIN",
        "IP",
    )
)


def serialize_aws_json_1_1(value: FleetProxyRuleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetProxyRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetProxyRuleType value: {data!r}")
    return cast(FleetProxyRuleType, data)
