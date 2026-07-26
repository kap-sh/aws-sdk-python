"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_global_secondary_index_settings_update

ReplicaGlobalSecondaryIndexSettingsUpdateList: TypeAlias = list[
    "capo_dynamodb.types.replica_global_secondary_index_settings_update.ReplicaGlobalSecondaryIndexSettingsUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexSettingsUpdateList,
) -> list:
    import capo_dynamodb.types.replica_global_secondary_index_settings_update

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.replica_global_secondary_index_settings_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ReplicaGlobalSecondaryIndexSettingsUpdateList:
    import capo_dynamodb.types.replica_global_secondary_index_settings_update

    out: ReplicaGlobalSecondaryIndexSettingsUpdateList = []
    for item in data:
        out.append(
            capo_dynamodb.types.replica_global_secondary_index_settings_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
