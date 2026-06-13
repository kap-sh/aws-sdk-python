"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorLocalResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

MonitorLocalResourceType: TypeAlias = Literal[
    "AWS::EC2::VPC",
    "AWS::AvailabilityZone",
    "AWS::EC2::Subnet",
    "AWS::Region",
    "AWS::EKS::Cluster",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS::EC2::VPC",
        "AWS::AvailabilityZone",
        "AWS::EC2::Subnet",
        "AWS::Region",
        "AWS::EKS::Cluster",
    )
)


def serialize_json(value: MonitorLocalResourceType) -> str:
    return value


def deserialize_json(data: str) -> MonitorLocalResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorLocalResourceType value: {data!r}")
    return cast(MonitorLocalResourceType, data)
