"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.workload_identity_token_type


class GetWorkloadAccessTokenResponse(TypedDict, closed=True):
    workload_access_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType"
    """<p>An opaque token representing the identity of both the workload and the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenResponse) -> dict:
    out: dict = {}
    out["workloadAccessToken"] = value["workload_access_token"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenResponse:
    out: GetWorkloadAccessTokenResponse = {}  # type: ignore[typeddict-item]
    if "workloadAccessToken" in data:
        out["workload_access_token"] = data["workloadAccessToken"]
    else:
        raise DeserializationError(
            "GetWorkloadAccessTokenResponse.workload_access_token required"
        )
    return out
