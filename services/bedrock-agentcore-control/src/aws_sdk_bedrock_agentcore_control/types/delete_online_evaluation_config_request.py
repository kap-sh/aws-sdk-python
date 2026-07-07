"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteOnlineEvaluationConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id


class DeleteOnlineEvaluationConfigRequest(TypedDict, closed=True):
    online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the online evaluation configuration to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOnlineEvaluationConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOnlineEvaluationConfigRequest:
    out: DeleteOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    return out
