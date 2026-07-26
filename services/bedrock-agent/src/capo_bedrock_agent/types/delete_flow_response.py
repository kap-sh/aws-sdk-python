"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_id


class DeleteFlowResponse(TypedDict, closed=True):
    id: "capo_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteFlowResponse:
    out: DeleteFlowResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteFlowResponse.id required")
    return out
