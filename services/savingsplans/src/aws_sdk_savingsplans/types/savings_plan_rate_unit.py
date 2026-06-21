"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateUnit``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SavingsPlanRateUnit) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateUnit:
    return cast(SavingsPlanRateUnit, data)
