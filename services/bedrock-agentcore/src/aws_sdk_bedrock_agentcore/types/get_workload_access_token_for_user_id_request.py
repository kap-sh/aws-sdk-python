"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenForUserIdRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.user_id_type
    import aws_sdk_bedrock_agentcore.types.workload_identity_name_type

class GetWorkloadAccessTokenForUserIdRequest(TypedDict):
    workload_name: "aws_sdk_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload from which you want to retrieve the access token.</p>"""
    user_id: "aws_sdk_bedrock_agentcore.types.user_id_type.UserIdType"
    """<p>The ID of the user for whom you are retrieving the access token.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenForUserIdRequest) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenForUserIdRequest:
    out: GetWorkloadAccessTokenForUserIdRequest = {}  # type: ignore[typeddict-item]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    else:
        raise DeserializationError("GetWorkloadAccessTokenForUserIdRequest.workload_name required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("GetWorkloadAccessTokenForUserIdRequest.user_id required")
    return out