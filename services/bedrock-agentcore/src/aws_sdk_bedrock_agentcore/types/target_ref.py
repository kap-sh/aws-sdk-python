"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TargetRef``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.target_name


class TargetRef(TypedDict):
    name: "aws_sdk_bedrock_agentcore.types.target_name.TargetName"
    """<p>The name of the gateway target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetRef) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TargetRef:
    out: TargetRef = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TargetRef.name required")
    return out
