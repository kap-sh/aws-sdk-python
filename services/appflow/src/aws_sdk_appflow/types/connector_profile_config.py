"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_profile_credentials
    import aws_sdk_appflow.types.connector_profile_properties


class ConnectorProfileConfig(TypedDict):
    connector_profile_properties: (
        "aws_sdk_appflow.types.connector_profile_properties.ConnectorProfileProperties"
    )
    """<p> The connector-specific properties of the profile configuration. </p>"""
    connector_profile_credentials: NotRequired[
        "aws_sdk_appflow.types.connector_profile_credentials.ConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required by each connector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileConfig) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.connector_profile_properties

    out["connectorProfileProperties"] = (
        aws_sdk_appflow.types.connector_profile_properties.serialize_json(
            value["connector_profile_properties"]
        )
    )
    if "connector_profile_credentials" in value:
        import aws_sdk_appflow.types.connector_profile_credentials

        out["connectorProfileCredentials"] = (
            aws_sdk_appflow.types.connector_profile_credentials.serialize_json(
                value["connector_profile_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfileConfig:
    out: ConnectorProfileConfig = {}  # type: ignore[typeddict-item]
    if "connectorProfileProperties" in data:
        import aws_sdk_appflow.types.connector_profile_properties

        out["connector_profile_properties"] = (
            aws_sdk_appflow.types.connector_profile_properties.deserialize_json(
                data["connectorProfileProperties"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectorProfileConfig.connector_profile_properties required"
        )
    if "connectorProfileCredentials" in data:
        import aws_sdk_appflow.types.connector_profile_credentials

        out["connector_profile_credentials"] = (
            aws_sdk_appflow.types.connector_profile_credentials.deserialize_json(
                data["connectorProfileCredentials"]
            )
        )
    return out
