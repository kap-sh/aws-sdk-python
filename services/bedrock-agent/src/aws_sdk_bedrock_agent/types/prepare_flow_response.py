"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PrepareFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_id
    import aws_sdk_bedrock_agent.types.flow_status


class PrepareFlowResponse(TypedDict, closed=True):
    id: "aws_sdk_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    status: "aws_sdk_bedrock_agent.types.flow_status.FlowStatus"
    """<p>The status of the flow. When you submit this request, the status will be <code>NotPrepared</code>. If preparation succeeds, the status becomes <code>Prepared</code>. If it fails, the status becomes <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrepareFlowResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_bedrock_agent.types.flow_status

    out["status"] = aws_sdk_bedrock_agent.types.flow_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> PrepareFlowResponse:
    out: PrepareFlowResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PrepareFlowResponse.id required")
    if "status" in data:
        import aws_sdk_bedrock_agent.types.flow_status

        out["status"] = aws_sdk_bedrock_agent.types.flow_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("PrepareFlowResponse.status required")
    return out
