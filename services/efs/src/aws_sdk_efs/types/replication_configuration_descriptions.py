"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationConfigurationDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.replication_configuration_description

ReplicationConfigurationDescriptions: TypeAlias = list[
    "aws_sdk_efs.types.replication_configuration_description.ReplicationConfigurationDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationDescriptions) -> list:
    import aws_sdk_efs.types.replication_configuration_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_efs.types.replication_configuration_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplicationConfigurationDescriptions:
    import aws_sdk_efs.types.replication_configuration_description

    out: ReplicationConfigurationDescriptions = []
    for item in data:
        out.append(
            aws_sdk_efs.types.replication_configuration_description.deserialize_json(
                item
            )
        )
    return out
