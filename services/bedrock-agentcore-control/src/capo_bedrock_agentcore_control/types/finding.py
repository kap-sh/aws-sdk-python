"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.finding_type
    import capo_bedrock_agentcore_control.types.string


class Finding(TypedDict, closed=True):
    type: NotRequired["capo_bedrock_agentcore_control.types.finding_type.FindingType"]
    """<p>The type or category of the finding. This classifies the finding as an error, warning, recommendation, or informational message to help users understand the severity and nature of the issue.</p>"""
    description: NotRequired["capo_bedrock_agentcore_control.types.string.String"]
    """<p>A human-readable description of the finding. This provides detailed information about the issue, recommendation, or validation result to help users understand and address the finding. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_bedrock_agentcore_control.types.finding_type

        out["type"] = capo_bedrock_agentcore_control.types.finding_type.serialize_json(
            value["type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock_agentcore_control.types.finding_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.finding_type.deserialize_json(
                data["type"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
