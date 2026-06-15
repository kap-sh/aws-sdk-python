"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticRoute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.target_name


class StaticRoute(TypedDict):
    target_name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the target to route requests to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticRoute) -> dict:
    out: dict = {}
    out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> StaticRoute:
    out: StaticRoute = {}  # type: ignore[typeddict-item]
    if "targetName" in data:
        out["target_name"] = data["targetName"]
    else:
        raise DeserializationError("StaticRoute.target_name required")
    return out
