"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorDestinationListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_destination_summary

ConnectorDestinationListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.connector_destination_summary.ConnectorDestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorDestinationListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.connector_destination_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.connector_destination_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConnectorDestinationListDefinition:
    import aws_sdk_iot_managed_integrations.types.connector_destination_summary

    out: ConnectorDestinationListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.connector_destination_summary.deserialize_json(
                item
            )
        )
    return out
