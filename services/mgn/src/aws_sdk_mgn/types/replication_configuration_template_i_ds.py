"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationConfigurationTemplateIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.replication_configuration_template_id

ReplicationConfigurationTemplateIDs: TypeAlias = list[
    "aws_sdk_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationTemplateIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> ReplicationConfigurationTemplateIDs:
    return list(data)
