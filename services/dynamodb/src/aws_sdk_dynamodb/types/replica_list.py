"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica

ReplicaList: TypeAlias = list["aws_sdk_dynamodb.types.replica.Replica"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaList) -> list:
    import aws_sdk_dynamodb.types.replica

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.replica.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaList:
    import aws_sdk_dynamodb.types.replica

    out: ReplicaList = []
    for item in data:
        out.append(aws_sdk_dynamodb.types.replica.deserialize_aws_json_1_0(item))
    return out
