"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorLocalResourceType``."""

from typing import Literal, TypeAlias, cast

MonitorLocalResourceType: TypeAlias = Literal[
    "AWS::EC2::VPC",
    "AWS::AvailabilityZone",
    "AWS::EC2::Subnet",
    "AWS::Region",
    "AWS::EKS::Cluster",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorLocalResourceType) -> str:
    return value


def deserialize_json(data: str) -> MonitorLocalResourceType:
    return cast(MonitorLocalResourceType, data)
