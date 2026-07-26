"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilterStatus``."""

from typing import Literal, TypeAlias, cast

RecommenderFilterStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderFilterStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommenderFilterStatus:
    return cast(RecommenderFilterStatus, data)
