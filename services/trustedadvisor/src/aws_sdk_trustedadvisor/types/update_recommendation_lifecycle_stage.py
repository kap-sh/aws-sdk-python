"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationLifecycleStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

UpdateRecommendationLifecycleStage: TypeAlias = Literal[
    "pending_response",
    "in_progress",
    "dismissed",
    "resolved",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending_response",
        "in_progress",
        "dismissed",
        "resolved",
    )
)


def serialize_json(value: UpdateRecommendationLifecycleStage) -> str:
    return value


def deserialize_json(data: str) -> UpdateRecommendationLifecycleStage:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateRecommendationLifecycleStage value: {data!r}"
        )
    return cast(UpdateRecommendationLifecycleStage, data)
