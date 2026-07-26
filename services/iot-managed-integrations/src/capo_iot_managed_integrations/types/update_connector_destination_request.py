"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateConnectorDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_config_update
    import capo_iot_managed_integrations.types.auth_type
    import capo_iot_managed_integrations.types.connector_destination_description
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.connector_destination_name
    import capo_iot_managed_integrations.types.secrets_manager


class UpdateConnectorDestinationRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    """<p>The unique identifier of the connector destination to update.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
    ]
    """<p>The new description to assign to the connector destination.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
    ]
    """<p>The new display name to assign to the connector destination.</p>"""
    auth_type: NotRequired["capo_iot_managed_integrations.types.auth_type.AuthType"]
    """<p>The new authentication type to use for the connector destination.</p>"""
    auth_config: NotRequired[
        "capo_iot_managed_integrations.types.auth_config_update.AuthConfigUpdate"
    ]
    """<p>The updated authentication configuration details for the connector destination.</p>"""
    secrets_manager: NotRequired[
        "capo_iot_managed_integrations.types.secrets_manager.SecretsManager"
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
        import capo_iot_managed_integrations.types.auth_type

        out["AuthType"] = capo_iot_managed_integrations.types.auth_type.serialize_json(
            value["auth_type"]
        )
    if "auth_config" in value:
        import capo_iot_managed_integrations.types.auth_config_update

        out["AuthConfig"] = (
            capo_iot_managed_integrations.types.auth_config_update.serialize_json(
                value["auth_config"]
            )
        )
    if "secrets_manager" in value:
        import capo_iot_managed_integrations.types.secrets_manager

        out["SecretsManager"] = (
            capo_iot_managed_integrations.types.secrets_manager.serialize_json(
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
        import capo_iot_managed_integrations.types.auth_type

        out["auth_type"] = (
            capo_iot_managed_integrations.types.auth_type.deserialize_json(
                data["AuthType"]
            )
        )
    if "AuthConfig" in data:
        import capo_iot_managed_integrations.types.auth_config_update

        out["auth_config"] = (
            capo_iot_managed_integrations.types.auth_config_update.deserialize_json(
                data["AuthConfig"]
            )
        )
    if "SecretsManager" in data:
        import capo_iot_managed_integrations.types.secrets_manager

        out["secrets_manager"] = (
            capo_iot_managed_integrations.types.secrets_manager.deserialize_json(
                data["SecretsManager"]
            )
        )
    return out
