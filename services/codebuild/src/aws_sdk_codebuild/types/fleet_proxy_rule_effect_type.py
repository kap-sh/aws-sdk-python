"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleEffectType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetProxyRuleEffectType: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: FleetProxyRuleEffectType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetProxyRuleEffectType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetProxyRuleEffectType value: {data!r}")
    return cast(FleetProxyRuleEffectType, data)
