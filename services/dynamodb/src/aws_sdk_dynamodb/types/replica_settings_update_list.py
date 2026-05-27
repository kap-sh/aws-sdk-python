"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_settings_update

ReplicaSettingsUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_settings_update.ReplicaSettingsUpdate"
]
