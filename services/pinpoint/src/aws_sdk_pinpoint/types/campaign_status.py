"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CampaignStatus) -> str:
    return value


def deserialize_json(data: str) -> CampaignStatus:
    return cast(CampaignStatus, data)
