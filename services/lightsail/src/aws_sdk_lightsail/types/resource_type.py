"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "ContainerService",
    "Instance",
    "StaticIp",
    "KeyPair",
    "InstanceSnapshot",
    "Domain",
    "PeeredVpc",
    "LoadBalancer",
    "LoadBalancerTlsCertificate",
    "Disk",
    "DiskSnapshot",
    "RelationalDatabase",
    "RelationalDatabaseSnapshot",
    "ExportSnapshotRecord",
    "CloudFormationStackRecord",
    "Alarm",
    "ContactMethod",
    "Distribution",
    "Certificate",
    "Bucket",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ContainerService",
        "Instance",
        "StaticIp",
        "KeyPair",
        "InstanceSnapshot",
        "Domain",
        "PeeredVpc",
        "LoadBalancer",
        "LoadBalancerTlsCertificate",
        "Disk",
        "DiskSnapshot",
        "RelationalDatabase",
        "RelationalDatabaseSnapshot",
        "ExportSnapshotRecord",
        "CloudFormationStackRecord",
        "Alarm",
        "ContactMethod",
        "Distribution",
        "Certificate",
        "Bucket",
    )
)


def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
