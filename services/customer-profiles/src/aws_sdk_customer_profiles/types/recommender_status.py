"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderStatus``."""

from typing import Literal, TypeAlias, cast

RecommenderStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "ACTIVE",
    "FAILED",
    "STOPPING",
    "INACTIVE",
    "STARTING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommenderStatus:
    return cast(RecommenderStatus, data)
