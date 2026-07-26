"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ReplicaStatusType``."""

from typing import Literal, TypeAlias, cast

ReplicaStatusType: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "INACTIVE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicaStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicaStatusType:
    return cast(ReplicaStatusType, data)
