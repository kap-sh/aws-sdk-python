"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingPublishingFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

FindingPublishingFrequency: TypeAlias = Literal[
    "FIFTEEN_MINUTES",
    "ONE_HOUR",
    "SIX_HOURS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIFTEEN_MINUTES",
        "ONE_HOUR",
        "SIX_HOURS",
    )
)


def serialize_json(value: FindingPublishingFrequency) -> str:
    return value


def deserialize_json(data: str) -> FindingPublishingFrequency:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FindingPublishingFrequency value: {data!r}"
        )
    return cast(FindingPublishingFrequency, data)
