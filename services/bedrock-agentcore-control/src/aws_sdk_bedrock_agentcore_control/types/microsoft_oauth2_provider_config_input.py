"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MicrosoftOauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_id_type
    import aws_sdk_bedrock_agentcore_control.types.default_client_secret_type
    import aws_sdk_bedrock_agentcore_control.types.secret_reference
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type
    import aws_sdk_bedrock_agentcore_control.types.tenant_id_type


class MicrosoftOauth2ProviderConfigInput(TypedDict, closed=True):
    client_id: "aws_sdk_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    """<p>The client ID for the Microsoft OAuth2 provider.</p>"""
    client_secret: "aws_sdk_bedrock_agentcore_control.types.default_client_secret_type.DefaultClientSecretType"
    """<p>The client secret for the Microsoft OAuth2 provider.</p>"""
    client_secret_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when <code>clientSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    client_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the client secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>"""
    tenant_id: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.tenant_id_type.TenantIdType"
    ]
    """<p>The Microsoft Entra ID (formerly Azure AD) tenant ID for your organization. This identifies the specific tenant within Microsoft's identity platform where your application is registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrosoftOauth2ProviderConfigInput) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value.get("client_secret", "")
    if "client_secret_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["clientSecretConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["client_secret_config"]
            )
        )
    if "client_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["clientSecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["client_secret_source"]
            )
        )
    if "tenant_id" in value:
        out["tenantId"] = value["tenant_id"]
    return out


def deserialize_json(data: dict) -> MicrosoftOauth2ProviderConfigInput:
    out: MicrosoftOauth2ProviderConfigInput = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "MicrosoftOauth2ProviderConfigInput.client_id required"
        )
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        out["client_secret"] = ""
    if "clientSecretConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["client_secret_config"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["clientSecretConfig"]
            )
        )
    if "clientSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["client_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["clientSecretSource"]
            )
        )
    if "tenantId" in data:
        out["tenant_id"] = data["tenantId"]
    return out
