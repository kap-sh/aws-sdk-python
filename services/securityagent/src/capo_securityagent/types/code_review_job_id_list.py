"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJobIdList``."""

from typing import TypeAlias

CodeReviewJobIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJobIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CodeReviewJobIdList:
    return list(data)
