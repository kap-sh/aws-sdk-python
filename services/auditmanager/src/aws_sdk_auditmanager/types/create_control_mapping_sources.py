"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateControlMappingSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.create_control_mapping_source

CreateControlMappingSources: TypeAlias = list[
    "aws_sdk_auditmanager.types.create_control_mapping_source.CreateControlMappingSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateControlMappingSources) -> list:
    import aws_sdk_auditmanager.types.create_control_mapping_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.create_control_mapping_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateControlMappingSources:
    import aws_sdk_auditmanager.types.create_control_mapping_source

    out: CreateControlMappingSources = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.create_control_mapping_source.deserialize_json(
                item
            )
        )
    return out
