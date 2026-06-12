"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanRateUnit: TypeAlias = Literal[
    "Hrs",
    "Lambda-GB-Second",
    "Request",
    "ACU-Hr",
    "ReadRequestUnits",
    "WriteRequestUnits",
    "ReadCapacityUnit-Hrs",
    "WriteCapacityUnit-Hrs",
    "ReplicatedWriteRequestUnits",
    "ReplicatedWriteCapacityUnit-Hrs",
    "GB-Hours",
    "DPU",
    "ElastiCacheProcessingUnit",
    "DCU-Hr",
    "NCU-hr",
    "OCU-hours",
    "Jobs",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Hrs",
        "Lambda-GB-Second",
        "Request",
        "ACU-Hr",
        "ReadRequestUnits",
        "WriteRequestUnits",
        "ReadCapacityUnit-Hrs",
        "WriteCapacityUnit-Hrs",
        "ReplicatedWriteRequestUnits",
        "ReplicatedWriteCapacityUnit-Hrs",
        "GB-Hours",
        "DPU",
        "ElastiCacheProcessingUnit",
        "DCU-Hr",
        "NCU-hr",
        "OCU-hours",
        "Jobs",
    )
)


def serialize_json(value: SavingsPlanRateUnit) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlanRateUnit value: {data!r}")
    return cast(SavingsPlanRateUnit, data)
