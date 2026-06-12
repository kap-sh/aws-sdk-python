"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InstancePropertyFilterKey: TypeAlias = Literal[
    "InstanceIds",
    "AgentVersion",
    "PingStatus",
    "PlatformTypes",
    "DocumentName",
    "ActivationIds",
    "IamRole",
    "ResourceType",
    "AssociationStatus",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceIds",
        "AgentVersion",
        "PingStatus",
        "PlatformTypes",
        "DocumentName",
        "ActivationIds",
        "IamRole",
        "ResourceType",
        "AssociationStatus",
    )
)


def serialize_aws_json_1_1(value: InstancePropertyFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePropertyFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstancePropertyFilterKey value: {data!r}")
    return cast(InstancePropertyFilterKey, data)
