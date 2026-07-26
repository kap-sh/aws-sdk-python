"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroupStatus``."""

from typing import Literal, TypeAlias, cast

TrafficDistributionGroupStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "CREATION_FAILED",
    "PENDING_DELETION",
    "DELETION_FAILED",
    "UPDATE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficDistributionGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> TrafficDistributionGroupStatus:
    return cast(TrafficDistributionGroupStatus, data)
