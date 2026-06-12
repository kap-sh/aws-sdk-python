"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetConnectorDestinationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_config
    import aws_sdk_iot_managed_integrations.types.auth_type
    import aws_sdk_iot_managed_integrations.types.cloud_connector_id
    import aws_sdk_iot_managed_integrations.types.connector_destination_description
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.connector_destination_name
    import aws_sdk_iot_managed_integrations.types.o_auth_complete_redirect_url
    import aws_sdk_iot_managed_integrations.types.secrets_manager


class GetConnectorDestinationResponse(TypedDict):
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
    ]
    """<p>The display name of the connector destination.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
    ]
    """<p>A description of the connector destination.</p>"""
    cloud_connector_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The identifier of the C2C connector.</p>"""
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The unique identifier of the connector destination.</p>"""
    auth_type: NotRequired["aws_sdk_iot_managed_integrations.types.auth_type.AuthType"]
    """<p>The authentication type used for the connector destination, which determines how credentials and access are managed.</p>"""
    auth_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.auth_config.AuthConfig"
    ]
    """<p>The authentication configuration details for the connector destination, including OAuth settings and other authentication parameters.</p>"""
    secrets_manager: NotRequired[
        "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
    ]
    """<p>The AWS Secrets Manager configuration used to securely store and manage sensitive information for the connector destination.</p>"""
    o_auth_complete_redirect_url: NotRequired[
        "aws_sdk_iot_managed_integrations.types.o_auth_complete_redirect_url.OAuthCompleteRedirectUrl"
    ]
    """<p>The URL where users are redirected after completing the OAuth authorization process for the connector destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorDestinationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "cloud_connector_id" in value:
        out["CloudConnectorId"] = value["cloud_connector_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "auth_type" in value:
        import aws_sdk_iot_managed_integrations.types.auth_type

        out["AuthType"] = (
            aws_sdk_iot_managed_integrations.types.auth_type.serialize_json(
                value["auth_type"]
            )
        )
    if "auth_config" in value:
        import aws_sdk_iot_managed_integrations.types.auth_config

        out["AuthConfig"] = (
            aws_sdk_iot_managed_integrations.types.auth_config.serialize_json(
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
    if "o_auth_complete_redirect_url" in value:
        out["OAuthCompleteRedirectUrl"] = value["o_auth_complete_redirect_url"]
    return out


def deserialize_json(data: dict) -> GetConnectorDestinationResponse:
    out: GetConnectorDestinationResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CloudConnectorId" in data:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "AuthType" in data:
        import aws_sdk_iot_managed_integrations.types.auth_type

        out["auth_type"] = (
            aws_sdk_iot_managed_integrations.types.auth_type.deserialize_json(
                data["AuthType"]
            )
        )
    if "AuthConfig" in data:
        import aws_sdk_iot_managed_integrations.types.auth_config

        out["auth_config"] = (
            aws_sdk_iot_managed_integrations.types.auth_config.deserialize_json(
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
    if "OAuthCompleteRedirectUrl" in data:
        out["o_auth_complete_redirect_url"] = data["OAuthCompleteRedirectUrl"]
    return out
