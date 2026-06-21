"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallRulesFailOpenType``."""

from typing import Literal, TypeAlias, cast

FirewallRulesFailOpenType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallRulesFailOpenType) -> str:
    return value


def deserialize_json(data: str) -> FirewallRulesFailOpenType:
    return cast(FirewallRulesFailOpenType, data)
