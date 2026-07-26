"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilitySchemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_schema_item

CapabilitySchemas: TypeAlias = list[
    "capo_iot_managed_integrations.types.capability_schema_item.CapabilitySchemaItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilitySchemas) -> list:
    import capo_iot_managed_integrations.types.capability_schema_item

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.capability_schema_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CapabilitySchemas:
    import capo_iot_managed_integrations.types.capability_schema_item

    out: CapabilitySchemas = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.capability_schema_item.deserialize_json(
                item
            )
        )
    return out
