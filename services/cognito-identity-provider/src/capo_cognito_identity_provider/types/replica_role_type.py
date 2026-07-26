"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ReplicaRoleType``."""

from typing import Literal, TypeAlias, cast

ReplicaRoleType: TypeAlias = Literal[
    "PRIMARY",
    "SECONDARY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicaRoleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicaRoleType:
    return cast(ReplicaRoleType, data)
