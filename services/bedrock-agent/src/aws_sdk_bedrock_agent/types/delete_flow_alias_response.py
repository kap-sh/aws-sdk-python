"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_alias_id
    import aws_sdk_bedrock_agent.types.flow_id


class DeleteFlowAliasResponse(TypedDict):
    flow_id: "aws_sdk_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow that the alias belongs to.</p>"""
    id: "aws_sdk_bedrock_agent.types.flow_alias_id.FlowAliasId"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowAliasResponse) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteFlowAliasResponse:
    out: DeleteFlowAliasResponse = {}  # type: ignore[typeddict-item]
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("DeleteFlowAliasResponse.flow_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteFlowAliasResponse.id required")
    return out
