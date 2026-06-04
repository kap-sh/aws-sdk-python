"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_settings_description

ReplicaSettingsDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_settings_description.ReplicaSettingsDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSettingsDescriptionList) -> list:
    import aws_sdk_dynamodb.types.replica_settings_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.replica_settings_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicaSettingsDescriptionList:
    import aws_sdk_dynamodb.types.replica_settings_description

    out: ReplicaSettingsDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.replica_settings_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
