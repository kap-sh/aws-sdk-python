"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableGlobalSecondaryIndexSettingsUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_table_global_secondary_index_settings_update

GlobalTableGlobalSecondaryIndexSettingsUpdateList: TypeAlias = list[
    "capo_dynamodb.types.global_table_global_secondary_index_settings_update.GlobalTableGlobalSecondaryIndexSettingsUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GlobalTableGlobalSecondaryIndexSettingsUpdateList,
) -> list:
    import capo_dynamodb.types.global_table_global_secondary_index_settings_update

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.global_table_global_secondary_index_settings_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> GlobalTableGlobalSecondaryIndexSettingsUpdateList:
    import capo_dynamodb.types.global_table_global_secondary_index_settings_update

    out: GlobalTableGlobalSecondaryIndexSettingsUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.global_table_global_secondary_index_settings_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
