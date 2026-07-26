"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_global_secondary_index_settings_description

ReplicaGlobalSecondaryIndexSettingsDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.replica_global_secondary_index_settings_description.ReplicaGlobalSecondaryIndexSettingsDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexSettingsDescriptionList,
) -> list:
    import capo_dynamodb.types.replica_global_secondary_index_settings_description

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.replica_global_secondary_index_settings_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ReplicaGlobalSecondaryIndexSettingsDescriptionList:
    import capo_dynamodb.types.replica_global_secondary_index_settings_description

    out: ReplicaGlobalSecondaryIndexSettingsDescriptionList = []
    for item in data:
        out.append(
            capo_dynamodb.types.replica_global_secondary_index_settings_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
