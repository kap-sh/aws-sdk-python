"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_description

ReplicaDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.replica_description.ReplicaDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaDescriptionList) -> list:
    import capo_dynamodb.types.replica_description

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.replica_description.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaDescriptionList:
    import capo_dynamodb.types.replica_description

    out: ReplicaDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.replica_description.deserialize_aws_json_1_0(item)
        )
    return out
