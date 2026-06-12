"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

CampaignStatus: TypeAlias = Literal[
    "SCHEDULED",
    "EXECUTING",
    "PENDING_NEXT_RUN",
    "COMPLETED",
    "PAUSED",
    "DELETED",
    "INVALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "EXECUTING",
        "PENDING_NEXT_RUN",
        "COMPLETED",
        "PAUSED",
        "DELETED",
        "INVALID",
    )
)


def serialize_json(value: CampaignStatus) -> str:
    return value


def deserialize_json(data: str) -> CampaignStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CampaignStatus value: {data!r}")
    return cast(CampaignStatus, data)
