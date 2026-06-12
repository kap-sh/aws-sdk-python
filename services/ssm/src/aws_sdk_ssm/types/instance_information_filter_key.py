"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InstanceInformationFilterKey: TypeAlias = Literal[
    "InstanceIds",
    "AgentVersion",
    "PingStatus",
    "PlatformTypes",
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
        "ActivationIds",
        "IamRole",
        "ResourceType",
        "AssociationStatus",
    )
)


def serialize_aws_json_1_1(value: InstanceInformationFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceInformationFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceInformationFilterKey value: {data!r}"
        )
    return cast(InstanceInformationFilterKey, data)
