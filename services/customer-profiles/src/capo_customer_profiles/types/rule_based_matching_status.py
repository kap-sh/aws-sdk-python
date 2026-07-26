"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RuleBasedMatchingStatus``."""

from typing import Literal, TypeAlias, cast

RuleBasedMatchingStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleBasedMatchingStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleBasedMatchingStatus:
    return cast(RuleBasedMatchingStatus, data)
