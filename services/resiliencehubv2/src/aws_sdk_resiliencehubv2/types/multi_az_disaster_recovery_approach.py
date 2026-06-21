"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#MultiAzDisasterRecoveryApproach``."""

from typing import Literal, TypeAlias, cast

MultiAzDisasterRecoveryApproach: TypeAlias = Literal[
    "ACTIVE_ACTIVE",
    "HOT_STANDBY",
    "WARM_STANDBY",
    "PILOT_LIGHT",
    "BACKUP_AND_RESTORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiAzDisasterRecoveryApproach) -> str:
    return value


def deserialize_json(data: str) -> MultiAzDisasterRecoveryApproach:
    return cast(MultiAzDisasterRecoveryApproach, data)
