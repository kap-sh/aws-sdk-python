"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_item

ConnectorList: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.connector_item.ConnectorItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorList) -> list:
    import aws_sdk_iot_managed_integrations.types.connector_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.connector_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectorList:
    import aws_sdk_iot_managed_integrations.types.connector_item

    out: ConnectorList = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.connector_item.deserialize_json(item)
        )
    return out
