"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: NodeFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeFilterKey value: {data!r}")
    return cast(NodeFilterKey, data)
