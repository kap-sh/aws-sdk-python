"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallRuleAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

FirewallRuleAction: TypeAlias = Literal[
    "ALLOW",
    "ALERT",
    "BLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "ALERT",
        "BLOCK",
    )
)


def serialize_json(value: FirewallRuleAction) -> str:
    return value


def deserialize_json(data: str) -> FirewallRuleAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallRuleAction value: {data!r}")
    return cast(FirewallRuleAction, data)
