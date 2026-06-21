"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorRemoteResourceType``."""

from typing import Literal, TypeAlias, cast

MonitorRemoteResourceType: TypeAlias = Literal[
    "AWS::EC2::VPC",
    "AWS::AvailabilityZone",
    "AWS::EC2::Subnet",
    "AWS::AWSService",
    "AWS::Region",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorRemoteResourceType) -> str:
    return value


def deserialize_json(data: str) -> MonitorRemoteResourceType:
    return cast(MonitorRemoteResourceType, data)
