"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateReplicaStatusType``."""

from typing import Literal, TypeAlias, cast

UpdateReplicaStatusType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateReplicaStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateReplicaStatusType:
    return cast(UpdateReplicaStatusType, data)
