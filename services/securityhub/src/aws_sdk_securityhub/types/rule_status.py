"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleStatus``."""

from typing import Literal, TypeAlias, cast

RuleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleStatus:
    return cast(RuleStatus, data)
