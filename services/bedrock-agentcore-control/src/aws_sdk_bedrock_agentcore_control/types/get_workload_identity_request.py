"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetWorkloadIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type

class GetWorkloadIdentityRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadIdentityRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetWorkloadIdentityRequest:
    out: GetWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetWorkloadIdentityRequest.name required")
    return out