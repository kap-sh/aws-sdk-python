"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Status of a recommendation</p>"""
RecommendationStatus: TypeAlias = Literal[
    "PROPOSED",
    "ACCEPTED",
    "REJECTED",
    "CLOSED",
    "COMPLETED",
    "UPDATE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
