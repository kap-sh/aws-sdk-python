"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationLifecycleStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

RecommendationLifecycleStage: TypeAlias = Literal[
    "in_progress",
    "pending_response",
    "dismissed",
    "resolved",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "in_progress",
        "pending_response",
        "dismissed",
        "resolved",
    )
)


def serialize_json(value: RecommendationLifecycleStage) -> str:
    return value


def deserialize_json(data: str) -> RecommendationLifecycleStage:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RecommendationLifecycleStage value: {data!r}"
        )
    return cast(RecommendationLifecycleStage, data)
