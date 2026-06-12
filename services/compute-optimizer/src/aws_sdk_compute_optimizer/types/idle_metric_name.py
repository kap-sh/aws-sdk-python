"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

IdleMetricName: TypeAlias = Literal[
    "CPU",
    "Memory",
    "NetworkOutBytesPerSecond",
    "NetworkInBytesPerSecond",
    "DatabaseConnections",
    "EBSVolumeReadIOPS",
    "EBSVolumeWriteIOPS",
    "VolumeReadOpsPerSecond",
    "VolumeWriteOpsPerSecond",
    "ActiveConnectionCount",
    "PacketsInFromSource",
    "PacketsInFromDestination",
    "ConsumedReadCapacityUnits",
    "ConsumedWriteCapacityUnits",
    "ConsumedChangeDataCaptureUnits",
    "NewConnections",
    "EngineCPUUtilization",
    "CacheHits",
    "CacheMisses",
    "KeyspaceHits",
    "KeyspaceMisses",
    "IsIdle",
    "UserConnected",
    "Invocations",
    "GetTypeCmds",
    "SetTypeCmds",
    "ElastiCacheProcessingUnits",
    "CurrConnections",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPU",
        "Memory",
        "NetworkOutBytesPerSecond",
        "NetworkInBytesPerSecond",
        "DatabaseConnections",
        "EBSVolumeReadIOPS",
        "EBSVolumeWriteIOPS",
        "VolumeReadOpsPerSecond",
        "VolumeWriteOpsPerSecond",
        "ActiveConnectionCount",
        "PacketsInFromSource",
        "PacketsInFromDestination",
        "ConsumedReadCapacityUnits",
        "ConsumedWriteCapacityUnits",
        "ConsumedChangeDataCaptureUnits",
        "NewConnections",
        "EngineCPUUtilization",
        "CacheHits",
        "CacheMisses",
        "KeyspaceHits",
        "KeyspaceMisses",
        "IsIdle",
        "UserConnected",
        "Invocations",
        "GetTypeCmds",
        "SetTypeCmds",
        "ElastiCacheProcessingUnits",
        "CurrConnections",
    )
)


def serialize_aws_json_1_0(value: IdleMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdleMetricName value: {data!r}")
    return cast(IdleMetricName, data)
