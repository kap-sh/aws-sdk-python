"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateConnectorDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_config_update
    import aws_sdk_iot_managed_integrations.types.auth_type
    import aws_sdk_iot_managed_integrations.types.connector_destination_description
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.connector_destination_name
    import aws_sdk_iot_managed_integrations.types.secrets_manager


class UpdateConnectorDestinationRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    """<p>The unique identifier of the connector destination to update.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
    ]
    """<p>The new description to assign to the connector destination.</p>"""
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
    ]
    """<p>The new display name to assign to the connector destination.</p>"""
    auth_type: NotRequired["aws_sdk_iot_managed_integrations.types.auth_type.AuthType"]
    """<p>The new authentication type to use for the connector destination.</p>"""
    auth_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.auth_config_update.AuthConfigUpdate"
    ]
    """<p>The updated authentication configuration details for the connector destination.</p>"""
    secrets_manager: NotRequired[
        "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
    ]
    """<p>The updated AWS Secrets Manager configuration for the connector destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorDestinationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "auth_type" in value:
        import aws_sdk_iot_managed_integrations.types.auth_type

        out["AuthType"] = (
            aws_sdk_iot_managed_integrations.types.auth_type.serialize_json(
                value["auth_type"]
            )
        )
    if "auth_config" in value:
        import aws_sdk_iot_managed_integrations.types.auth_config_update

        out["AuthConfig"] = (
            aws_sdk_iot_managed_integrations.types.auth_config_update.serialize_json(
                value["auth_config"]
            )
        )
    if "secrets_manager" in value:
        import aws_sdk_iot_managed_integrations.types.secrets_manager

        out["SecretsManager"] = (
            aws_sdk_iot_managed_integrations.types.secrets_manager.serialize_json(
                value["secrets_manager"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorDestinationRequest:
    out: UpdateConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "AuthType" in data:
        import aws_sdk_iot_managed_integrations.types.auth_type

        out["auth_type"] = (
            aws_sdk_iot_managed_integrations.types.auth_type.deserialize_json(
                data["AuthType"]
            )
        )
    if "AuthConfig" in data:
        import aws_sdk_iot_managed_integrations.types.auth_config_update

        out["auth_config"] = (
            aws_sdk_iot_managed_integrations.types.auth_config_update.deserialize_json(
                data["AuthConfig"]
            )
        )
    if "SecretsManager" in data:
        import aws_sdk_iot_managed_integrations.types.secrets_manager

        out["secrets_manager"] = (
            aws_sdk_iot_managed_integrations.types.secrets_manager.deserialize_json(
                data["SecretsManager"]
            )
        )
    return out
