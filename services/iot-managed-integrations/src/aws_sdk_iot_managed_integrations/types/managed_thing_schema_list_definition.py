"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingSchemaListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_item

ManagedThingSchemaListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_item.ManagedThingSchemaListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingSchemaListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedThingSchemaListDefinition:
    import aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_item

    out: ManagedThingSchemaListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_item.deserialize_json(
                item
            )
        )
    return out
