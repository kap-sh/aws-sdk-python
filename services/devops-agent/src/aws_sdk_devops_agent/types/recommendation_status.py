"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PROPOSED",
        "ACCEPTED",
        "REJECTED",
        "CLOSED",
        "COMPLETED",
        "UPDATE_IN_PROGRESS",
    )
)


def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStatus value: {data!r}")
    return cast(RecommendationStatus, data)
