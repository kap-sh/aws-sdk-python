"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListOauth2CredentialProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_providers


class ListOauth2CredentialProvidersResponse(TypedDict):
    credential_providers: "aws_sdk_bedrock_agentcore_control.types.oauth2_credential_providers.Oauth2CredentialProviders"
    """<p>The list of OAuth2 credential providers.</p>"""
    next_token: NotRequired["str"]
    """<p>Pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOauth2CredentialProvidersResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_providers

    out["credentialProviders"] = (
        aws_sdk_bedrock_agentcore_control.types.oauth2_credential_providers.serialize_json(
            value["credential_providers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOauth2CredentialProvidersResponse:
    out: ListOauth2CredentialProvidersResponse = {}  # type: ignore[typeddict-item]
    if "credentialProviders" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_providers

        out["credential_providers"] = (
            aws_sdk_bedrock_agentcore_control.types.oauth2_credential_providers.deserialize_json(
                data["credentialProviders"]
            )
        )
    else:
        raise DeserializationError(
            "ListOauth2CredentialProvidersResponse.credential_providers required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
