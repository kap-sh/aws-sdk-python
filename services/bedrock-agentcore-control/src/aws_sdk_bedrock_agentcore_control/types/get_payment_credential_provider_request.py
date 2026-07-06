"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPaymentCredentialProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name


class GetPaymentCredentialProviderRequest(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the payment credential provider to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentCredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetPaymentCredentialProviderRequest:
    out: GetPaymentCredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPaymentCredentialProviderRequest.name required")
    return out
