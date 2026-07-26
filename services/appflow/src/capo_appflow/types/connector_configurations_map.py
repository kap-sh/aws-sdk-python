"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorConfigurationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_configuration
    import capo_appflow.types.connector_type

ConnectorConfigurationsMap: TypeAlias = dict[
    "capo_appflow.types.connector_type.ConnectorType",
    "capo_appflow.types.connector_configuration.ConnectorConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectorConfigurationsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appflow.types.connector_configuration
        import capo_appflow.types.connector_type

        out[capo_appflow.types.connector_type.serialize_json(key)] = (
            capo_appflow.types.connector_configuration.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ConnectorConfigurationsMap:
    out: ConnectorConfigurationsMap = {}
    for key, value in data.items():
        import capo_appflow.types.connector_configuration
        import capo_appflow.types.connector_type

        out[capo_appflow.types.connector_type.deserialize_json(key)] = (
            capo_appflow.types.connector_configuration.deserialize_json(value)
        )
    return out
