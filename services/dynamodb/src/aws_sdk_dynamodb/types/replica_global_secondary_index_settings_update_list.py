"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update

ReplicaGlobalSecondaryIndexSettingsUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update.ReplicaGlobalSecondaryIndexSettingsUpdate"
]
