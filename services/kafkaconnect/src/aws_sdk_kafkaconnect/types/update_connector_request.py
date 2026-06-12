"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.capacity_update
    import aws_sdk_kafkaconnect.types.connector_configuration_update


class UpdateConnectorRequest(TypedDict):
    capacity: NotRequired["aws_sdk_kafkaconnect.types.capacity_update.CapacityUpdate"]
    """<p>The target capacity.</p>"""
    connector_configuration: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_configuration_update.ConnectorConfigurationUpdate"
    ]
    """<p>A map of keys to values that represent the configuration for the connector.</p>"""
    connector_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to update.</p>"""
    current_version: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The current version of the connector that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRequest) -> dict:
    out: dict = {}
    if "capacity" in value:
        import aws_sdk_kafkaconnect.types.capacity_update

        out["capacity"] = aws_sdk_kafkaconnect.types.capacity_update.serialize_json(
            value["capacity"]
        )
    if "connector_configuration" in value:
        import aws_sdk_kafkaconnect.types.connector_configuration_update

        out["connectorConfiguration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration_update.serialize_json(
                value["connector_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorRequest:
    out: UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        import aws_sdk_kafkaconnect.types.capacity_update

        out["capacity"] = aws_sdk_kafkaconnect.types.capacity_update.deserialize_json(
            data["capacity"]
        )
    if "connectorConfiguration" in data:
        import aws_sdk_kafkaconnect.types.connector_configuration_update

        out["connector_configuration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration_update.deserialize_json(
                data["connectorConfiguration"]
            )
        )
    return out
