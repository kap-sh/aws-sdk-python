"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LinkedinOauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_id_type
    import aws_sdk_bedrock_agentcore_control.types.default_client_secret_type
    import aws_sdk_bedrock_agentcore_control.types.secret_reference
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type


class LinkedinOauth2ProviderConfigInput(TypedDict):
    client_id: "aws_sdk_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    """<p>The client ID for the LinkedIn OAuth2 provider. This identifier is assigned by LinkedIn when you register your application.</p>"""
    client_secret: "aws_sdk_bedrock_agentcore_control.types.default_client_secret_type.DefaultClientSecretType"
    """<p>The client secret for the LinkedIn OAuth2 provider. This secret is assigned by LinkedIn and used along with the client ID to authenticate your application.</p>"""
    client_secret_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the AWS Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when <code>clientSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    client_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the client secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedinOauth2ProviderConfigInput) -> dict:
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
    return out


def deserialize_json(data: dict) -> LinkedinOauth2ProviderConfigInput:
    out: LinkedinOauth2ProviderConfigInput = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "LinkedinOauth2ProviderConfigInput.client_id required"
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
    return out
