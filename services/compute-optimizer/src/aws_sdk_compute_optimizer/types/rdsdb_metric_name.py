"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSDBMetricName: TypeAlias = Literal[
    "CPU",
    "Memory",
    "EBSVolumeStorageSpaceUtilization",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
    "EBSVolumeReadIOPS",
    "EBSVolumeWriteIOPS",
    "EBSVolumeReadThroughput",
    "EBSVolumeWriteThroughput",
    "DatabaseConnections",
    "StorageNetworkReceiveThroughput",
    "StorageNetworkTransmitThroughput",
    "AuroraMemoryHealthState",
    "AuroraMemoryNumDeclinedSql",
    "AuroraMemoryNumKillConnTotal",
    "AuroraMemoryNumKillQueryTotal",
    "ReadIOPSEphemeralStorage",
    "WriteIOPSEphemeralStorage",
    "VolumeReadIOPs",
    "VolumeBytesUsed",
    "VolumeWriteIOPs",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPU",
        "Memory",
        "EBSVolumeStorageSpaceUtilization",
        "NetworkReceiveThroughput",
        "NetworkTransmitThroughput",
        "EBSVolumeReadIOPS",
        "EBSVolumeWriteIOPS",
        "EBSVolumeReadThroughput",
        "EBSVolumeWriteThroughput",
        "DatabaseConnections",
        "StorageNetworkReceiveThroughput",
        "StorageNetworkTransmitThroughput",
        "AuroraMemoryHealthState",
        "AuroraMemoryNumDeclinedSql",
        "AuroraMemoryNumKillConnTotal",
        "AuroraMemoryNumKillQueryTotal",
        "ReadIOPSEphemeralStorage",
        "WriteIOPSEphemeralStorage",
        "VolumeReadIOPs",
        "VolumeBytesUsed",
        "VolumeWriteIOPs",
    )
)


def serialize_aws_json_1_0(value: RDSDBMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSDBMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RDSDBMetricName value: {data!r}")
    return cast(RDSDBMetricName, data)
