"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationFilterKey``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: InstanceInformationFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceInformationFilterKey:
    return cast(InstanceInformationFilterKey, data)
