"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallRulesFailOpenType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

FirewallRulesFailOpenType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: FirewallRulesFailOpenType) -> str:
    return value


def deserialize_json(data: str) -> FirewallRulesFailOpenType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallRulesFailOpenType value: {data!r}")
    return cast(FirewallRulesFailOpenType, data)
