"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetOauth2CredentialProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name


class GetOauth2CredentialProviderRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOauth2CredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetOauth2CredentialProviderRequest:
    out: GetOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetOauth2CredentialProviderRequest.name required")
    return out
