"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourceApiKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.credential_provider_name
    import aws_sdk_bedrock_agentcore.types.workload_identity_token_type


class GetResourceApiKeyRequest(TypedDict):
    workload_identity_token: "aws_sdk_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType"
    """<p>The identity token of the workload from which you want to retrieve the API key.</p>"""
    resource_credential_provider_name: "aws_sdk_bedrock_agentcore.types.credential_provider_name.CredentialProviderName"
    """<p>The credential provider name for the resource from which you are retrieving the API key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceApiKeyRequest) -> dict:
    out: dict = {}
    out["workloadIdentityToken"] = value["workload_identity_token"]
    out["resourceCredentialProviderName"] = value["resource_credential_provider_name"]
    return out


def deserialize_json(data: dict) -> GetResourceApiKeyRequest:
    out: GetResourceApiKeyRequest = {}  # type: ignore[typeddict-item]
    if "workloadIdentityToken" in data:
        out["workload_identity_token"] = data["workloadIdentityToken"]
    else:
        raise DeserializationError(
            "GetResourceApiKeyRequest.workload_identity_token required"
        )
    if "resourceCredentialProviderName" in data:
        out["resource_credential_provider_name"] = data[
            "resourceCredentialProviderName"
        ]
    else:
        raise DeserializationError(
            "GetResourceApiKeyRequest.resource_credential_provider_name required"
        )
    return out
