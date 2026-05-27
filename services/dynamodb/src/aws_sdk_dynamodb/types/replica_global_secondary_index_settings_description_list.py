"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description

ReplicaGlobalSecondaryIndexSettingsDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description.ReplicaGlobalSecondaryIndexSettingsDescription"
]
