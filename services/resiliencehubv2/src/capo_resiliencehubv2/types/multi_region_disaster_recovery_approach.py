"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#MultiRegionDisasterRecoveryApproach``."""

from typing import Literal, TypeAlias, cast

MultiRegionDisasterRecoveryApproach: TypeAlias = Literal[
    "ACTIVE_ACTIVE",
    "HOT_STANDBY",
    "WARM_STANDBY",
    "PILOT_LIGHT",
    "BACKUP_AND_RESTORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiRegionDisasterRecoveryApproach) -> str:
    return value


def deserialize_json(data: str) -> MultiRegionDisasterRecoveryApproach:
    return cast(MultiRegionDisasterRecoveryApproach, data)
