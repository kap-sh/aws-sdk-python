"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#MultiAzDisasterRecoveryApproach``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

MultiAzDisasterRecoveryApproach: TypeAlias = Literal[
    "ACTIVE_ACTIVE",
    "HOT_STANDBY",
    "WARM_STANDBY",
    "PILOT_LIGHT",
    "BACKUP_AND_RESTORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE_ACTIVE",
        "HOT_STANDBY",
        "WARM_STANDBY",
        "PILOT_LIGHT",
        "BACKUP_AND_RESTORE",
    )
)


def serialize_json(value: MultiAzDisasterRecoveryApproach) -> str:
    return value


def deserialize_json(data: str) -> MultiAzDisasterRecoveryApproach:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MultiAzDisasterRecoveryApproach value: {data!r}"
        )
    return cast(MultiAzDisasterRecoveryApproach, data)
