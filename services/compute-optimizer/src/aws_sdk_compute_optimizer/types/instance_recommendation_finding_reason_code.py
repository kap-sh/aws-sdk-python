"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendationFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

InstanceRecommendationFindingReasonCode: TypeAlias = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NetworkPPSOverprovisioned",
    "NetworkPPSUnderprovisioned",
    "DiskIOPSOverprovisioned",
    "DiskIOPSUnderprovisioned",
    "DiskThroughputOverprovisioned",
    "DiskThroughputUnderprovisioned",
    "GPUUnderprovisioned",
    "GPUOverprovisioned",
    "GPUMemoryUnderprovisioned",
    "GPUMemoryOverprovisioned",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPUOverprovisioned",
        "CPUUnderprovisioned",
        "MemoryOverprovisioned",
        "MemoryUnderprovisioned",
        "EBSThroughputOverprovisioned",
        "EBSThroughputUnderprovisioned",
        "EBSIOPSOverprovisioned",
        "EBSIOPSUnderprovisioned",
        "NetworkBandwidthOverprovisioned",
        "NetworkBandwidthUnderprovisioned",
        "NetworkPPSOverprovisioned",
        "NetworkPPSUnderprovisioned",
        "DiskIOPSOverprovisioned",
        "DiskIOPSUnderprovisioned",
        "DiskThroughputOverprovisioned",
        "DiskThroughputUnderprovisioned",
        "GPUUnderprovisioned",
        "GPUOverprovisioned",
        "GPUMemoryUnderprovisioned",
        "GPUMemoryOverprovisioned",
    )
)


def serialize_aws_json_1_0(value: InstanceRecommendationFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceRecommendationFindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceRecommendationFindingReasonCode value: {data!r}"
        )
    return cast(InstanceRecommendationFindingReasonCode, data)
