"""Generated from Smithy shape ``com.amazonaws.mpa#ApproverLastActivity``."""

from typing import Literal, TypeAlias, cast

ApproverLastActivity: TypeAlias = Literal[
    "VOTED",
    "BASELINED",
    "RESPONDED_TO_INVITATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApproverLastActivity) -> str:
    return value


def deserialize_json(data: str) -> ApproverLastActivity:
    return cast(ApproverLastActivity, data)
