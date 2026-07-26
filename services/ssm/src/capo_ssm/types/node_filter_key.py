"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterKey``."""

from typing import Literal, TypeAlias, cast

NodeFilterKey: TypeAlias = Literal[
    "AgentType",
    "AgentVersion",
    "ComputerName",
    "InstanceId",
    "InstanceStatus",
    "IpAddress",
    "ManagedStatus",
    "PlatformName",
    "PlatformType",
    "PlatformVersion",
    "ResourceType",
    "OrganizationalUnitId",
    "OrganizationalUnitPath",
    "Region",
    "AccountId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeFilterKey:
    return cast(NodeFilterKey, data)
