"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePaymentCredentialProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name

class DeletePaymentCredentialProviderRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the payment credential provider to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentCredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeletePaymentCredentialProviderRequest:
    out: DeletePaymentCredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeletePaymentCredentialProviderRequest.name required")
    return out