"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallRuleAction``."""

from typing import Literal, TypeAlias, cast

FirewallRuleAction: TypeAlias = Literal[
    "ALLOW",
    "ALERT",
    "BLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallRuleAction) -> str:
    return value


def deserialize_json(data: str) -> FirewallRuleAction:
    return cast(FirewallRuleAction, data)
