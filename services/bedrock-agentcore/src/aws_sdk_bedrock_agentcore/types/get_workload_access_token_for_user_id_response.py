"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenForUserIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.workload_identity_token_type


class GetWorkloadAccessTokenForUserIdResponse(TypedDict, closed=True):
    workload_access_token: "aws_sdk_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType"
    """<p>The access token for the specified workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenForUserIdResponse) -> dict:
    out: dict = {}
    out["workloadAccessToken"] = value["workload_access_token"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenForUserIdResponse:
    out: GetWorkloadAccessTokenForUserIdResponse = {}  # type: ignore[typeddict-item]
    if "workloadAccessToken" in data:
        out["workload_access_token"] = data["workloadAccessToken"]
    else:
        raise DeserializationError(
            "GetWorkloadAccessTokenForUserIdResponse.workload_access_token required"
        )
    return out
