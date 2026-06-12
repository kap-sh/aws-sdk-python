"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorConfigurationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_configuration
    import aws_sdk_appflow.types.connector_type

ConnectorConfigurationsMap: TypeAlias = dict[
    "aws_sdk_appflow.types.connector_type.ConnectorType",
    "aws_sdk_appflow.types.connector_configuration.ConnectorConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectorConfigurationsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_appflow.types.connector_configuration
        import aws_sdk_appflow.types.connector_type

        out[aws_sdk_appflow.types.connector_type.serialize_json(key)] = (
            aws_sdk_appflow.types.connector_configuration.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ConnectorConfigurationsMap:
    out: ConnectorConfigurationsMap = {}
    for key, value in data.items():
        import aws_sdk_appflow.types.connector_configuration
        import aws_sdk_appflow.types.connector_type

        out[aws_sdk_appflow.types.connector_type.deserialize_json(key)] = (
            aws_sdk_appflow.types.connector_configuration.deserialize_json(value)
        )
    return out
