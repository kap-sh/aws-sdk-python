"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteOauth2CredentialProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_name


class DeleteOauth2CredentialProviderRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOauth2CredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteOauth2CredentialProviderRequest:
    out: DeleteOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "DeleteOauth2CredentialProviderRequest.name required"
        )
    return out
