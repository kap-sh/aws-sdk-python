"""Generated from Smithy shape ``com.amazonaws.connect#RulePublishStatus``."""

from typing import Literal, TypeAlias, cast

RulePublishStatus: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RulePublishStatus) -> str:
    return value


def deserialize_json(data: str) -> RulePublishStatus:
    return cast(RulePublishStatus, data)
