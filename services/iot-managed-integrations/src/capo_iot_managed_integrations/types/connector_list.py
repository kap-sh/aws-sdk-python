"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.connector_item

ConnectorList: TypeAlias = list[
    "capo_iot_managed_integrations.types.connector_item.ConnectorItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorList) -> list:
    import capo_iot_managed_integrations.types.connector_item

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.connector_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectorList:
    import capo_iot_managed_integrations.types.connector_item

    out: ConnectorList = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.connector_item.deserialize_json(item)
        )
    return out
