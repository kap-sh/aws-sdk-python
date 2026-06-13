"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorRemoteResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

MonitorRemoteResourceType: TypeAlias = Literal[
    "AWS::EC2::VPC",
    "AWS::AvailabilityZone",
    "AWS::EC2::Subnet",
    "AWS::AWSService",
    "AWS::Region",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS::EC2::VPC",
        "AWS::AvailabilityZone",
        "AWS::EC2::Subnet",
        "AWS::AWSService",
        "AWS::Region",
    )
)


def serialize_json(value: MonitorRemoteResourceType) -> str:
    return value


def deserialize_json(data: str) -> MonitorRemoteResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorRemoteResourceType value: {data!r}")
    return cast(MonitorRemoteResourceType, data)
