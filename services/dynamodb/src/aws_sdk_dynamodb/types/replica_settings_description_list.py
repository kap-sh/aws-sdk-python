"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_settings_description

ReplicaSettingsDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_settings_description.ReplicaSettingsDescription"
]
