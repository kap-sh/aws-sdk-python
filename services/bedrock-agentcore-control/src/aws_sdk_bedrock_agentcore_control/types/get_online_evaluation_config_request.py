"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetOnlineEvaluationConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id

class GetOnlineEvaluationConfigRequest(TypedDict):
    online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration to retrieve. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetOnlineEvaluationConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOnlineEvaluationConfigRequest:
    out: GetOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    return out