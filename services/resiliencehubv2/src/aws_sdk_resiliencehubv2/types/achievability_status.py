"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AchievabilityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

AchievabilityStatus: TypeAlias = Literal[
    "ACHIEVABLE",
    "NOT_ACHIEVABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACHIEVABLE",
        "NOT_ACHIEVABLE",
    )
)


def serialize_json(value: AchievabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> AchievabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AchievabilityStatus value: {data!r}")
    return cast(AchievabilityStatus, data)
