"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

NodeAttributeName: TypeAlias = Literal[
    "AgentVersion",
    "PlatformName",
    "PlatformType",
    "PlatformVersion",
    "Region",
    "ResourceType",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AgentVersion",
        "PlatformName",
        "PlatformType",
        "PlatformVersion",
        "Region",
        "ResourceType",
    )
)


def serialize_aws_json_1_1(value: NodeAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeAttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeAttributeName value: {data!r}")
    return cast(NodeAttributeName, data)
