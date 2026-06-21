"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterKey``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: InstancePropertyFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePropertyFilterKey:
    return cast(InstancePropertyFilterKey, data)
