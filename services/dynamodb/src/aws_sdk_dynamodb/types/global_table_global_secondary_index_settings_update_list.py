"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableGlobalSecondaryIndexSettingsUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_global_secondary_index_settings_update

GlobalTableGlobalSecondaryIndexSettingsUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_table_global_secondary_index_settings_update.GlobalTableGlobalSecondaryIndexSettingsUpdate"
]
