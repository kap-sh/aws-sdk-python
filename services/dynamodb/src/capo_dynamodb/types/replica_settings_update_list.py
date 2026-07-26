"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_settings_update

ReplicaSettingsUpdateList: TypeAlias = list[
    "capo_dynamodb.types.replica_settings_update.ReplicaSettingsUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSettingsUpdateList) -> list:
    import capo_dynamodb.types.replica_settings_update

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.replica_settings_update.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaSettingsUpdateList:
    import capo_dynamodb.types.replica_settings_update

    out: ReplicaSettingsUpdateList = []
    for item in data:
        out.append(
            capo_dynamodb.types.replica_settings_update.deserialize_aws_json_1_0(item)
        )
    return out
