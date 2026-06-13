"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

RecommendationType: TypeAlias = Literal[
    "standard",
    "priority",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "priority",
    )
)


def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationType value: {data!r}")
    return cast(RecommendationType, data)
