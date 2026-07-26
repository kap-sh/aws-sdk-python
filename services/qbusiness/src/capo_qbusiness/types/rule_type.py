"""Generated from Smithy shape ``com.amazonaws.qbusiness#RuleType``."""

from typing import Literal, TypeAlias, cast

RuleType: TypeAlias = Literal[
    "CONTENT_BLOCKER_RULE",
    "CONTENT_RETRIEVAL_RULE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    return cast(RuleType, data)
