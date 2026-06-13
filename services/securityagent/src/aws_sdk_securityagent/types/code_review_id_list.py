"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewIdList``."""

from typing import TypeAlias

CodeReviewIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CodeReviewIdList:
    return list(data)
