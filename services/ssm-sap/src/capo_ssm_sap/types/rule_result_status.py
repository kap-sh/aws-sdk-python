"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleResultStatus``."""

from typing import Literal, TypeAlias, cast

RuleResultStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "WARNING",
    "INFO",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleResultStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleResultStatus:
    return cast(RuleResultStatus, data)
