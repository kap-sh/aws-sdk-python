"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleStatusV2``."""

from typing import Literal, TypeAlias, cast

RuleStatusV2: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleStatusV2) -> str:
    return value


def deserialize_json(data: str) -> RuleStatusV2:
    return cast(RuleStatusV2, data)
