"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GatewayFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.target_path_list

class GatewayFilter(TypedDict):
    target_paths: NotRequired["aws_sdk_bedrock_agentcore.types.target_path_list.TargetPathList"]
    """<p>A list of target path patterns to include in the A/B test.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GatewayFilter) -> dict:
    out: dict = {}
    if "target_paths" in value:
        import aws_sdk_bedrock_agentcore.types.target_path_list
        out["targetPaths"] = aws_sdk_bedrock_agentcore.types.target_path_list.serialize_json(value["target_paths"])
    return out


def deserialize_json(data: dict) -> GatewayFilter:
    out: GatewayFilter = {}  # type: ignore[typeddict-item]
    if "targetPaths" in data:
        import aws_sdk_bedrock_agentcore.types.target_path_list
        out["target_paths"] = aws_sdk_bedrock_agentcore.types.target_path_list.deserialize_json(data["targetPaths"])
    return out