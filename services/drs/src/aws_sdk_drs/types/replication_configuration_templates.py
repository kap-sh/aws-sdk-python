"""Generated from Smithy shape ``com.amazonaws.drs#ReplicationConfigurationTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.replication_configuration_template

ReplicationConfigurationTemplates: TypeAlias = list[
    "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationTemplates) -> list:
    import aws_sdk_drs.types.replication_configuration_template

    out: list = []
    for item in value:
        out.append(
            aws_sdk_drs.types.replication_configuration_template.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplicationConfigurationTemplates:
    import aws_sdk_drs.types.replication_configuration_template

    out: ReplicationConfigurationTemplates = []
    for item in data:
        out.append(
            aws_sdk_drs.types.replication_configuration_template.deserialize_json(item)
        )
    return out
