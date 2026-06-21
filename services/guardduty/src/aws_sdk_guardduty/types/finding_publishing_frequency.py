"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingPublishingFrequency``."""

from typing import Literal, TypeAlias, cast

FindingPublishingFrequency: TypeAlias = Literal[
    "FIFTEEN_MINUTES",
    "ONE_HOUR",
    "SIX_HOURS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingPublishingFrequency) -> str:
    return value


def deserialize_json(data: str) -> FindingPublishingFrequency:
    return cast(FindingPublishingFrequency, data)
