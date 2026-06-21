"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RuleHealth``."""

from typing import Literal, TypeAlias, cast

RuleHealth: TypeAlias = Literal[
    "Healthy",
    "Unhealthy",
    "Provisioning",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleHealth) -> str:
    return value


def deserialize_json(data: str) -> RuleHealth:
    return cast(RuleHealth, data)
