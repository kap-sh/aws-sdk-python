"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSStorageFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

RDSStorageFindingReasonCode: TypeAlias = Literal[
    "EBSVolumeAllocatedStorageUnderprovisioned",
    "EBSVolumeThroughputUnderprovisioned",
    "EBSVolumeIOPSOverprovisioned",
    "EBSVolumeThroughputOverprovisioned",
    "NewGenerationStorageTypeAvailable",
    "DBClusterStorageOptionAvailable",
    "DBClusterStorageSavingsAvailable",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSStorageFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSStorageFindingReasonCode:
    return cast(RDSStorageFindingReasonCode, data)
