"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSInstanceFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSInstanceFindingReasonCode: TypeAlias = Literal[
    "CPUOverprovisioned",
    "NetworkBandwidthOverprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "CPUUnderprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "EBSThroughputUnderprovisioned",
    "NewGenerationDBInstanceClassAvailable",
    "NewEngineVersionAvailable",
    "DBClusterWriterUnderprovisioned",
    "MemoryUnderprovisioned",
    "InstanceStorageReadIOPSUnderprovisioned",
    "InstanceStorageWriteIOPSUnderprovisioned",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPUOverprovisioned",
        "NetworkBandwidthOverprovisioned",
        "EBSIOPSOverprovisioned",
        "EBSIOPSUnderprovisioned",
        "EBSThroughputOverprovisioned",
        "CPUUnderprovisioned",
        "NetworkBandwidthUnderprovisioned",
        "EBSThroughputUnderprovisioned",
        "NewGenerationDBInstanceClassAvailable",
        "NewEngineVersionAvailable",
        "DBClusterWriterUnderprovisioned",
        "MemoryUnderprovisioned",
        "InstanceStorageReadIOPSUnderprovisioned",
        "InstanceStorageWriteIOPSUnderprovisioned",
    )
)


def serialize_aws_json_1_0(value: RDSInstanceFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSInstanceFindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RDSInstanceFindingReasonCode value: {data!r}"
        )
    return cast(RDSInstanceFindingReasonCode, data)
