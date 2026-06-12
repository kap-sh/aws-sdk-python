"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSStorageFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "EBSVolumeAllocatedStorageUnderprovisioned",
        "EBSVolumeThroughputUnderprovisioned",
        "EBSVolumeIOPSOverprovisioned",
        "EBSVolumeThroughputOverprovisioned",
        "NewGenerationStorageTypeAvailable",
        "DBClusterStorageOptionAvailable",
        "DBClusterStorageSavingsAvailable",
    )
)


def serialize_aws_json_1_0(value: RDSStorageFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSStorageFindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RDSStorageFindingReasonCode value: {data!r}"
        )
    return cast(RDSStorageFindingReasonCode, data)
