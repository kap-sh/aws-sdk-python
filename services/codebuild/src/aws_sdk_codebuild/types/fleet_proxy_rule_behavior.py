"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetProxyRuleBehavior: TypeAlias = Literal[
    "ALLOW_ALL",
    "DENY_ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW_ALL",
        "DENY_ALL",
    )
)


def serialize_aws_json_1_1(value: FleetProxyRuleBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetProxyRuleBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetProxyRuleBehavior value: {data!r}")
    return cast(FleetProxyRuleBehavior, data)
