"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStreamUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.automation_stream_status


class AutomationStreamUpdate(TypedDict, closed=True):
    stream_status: NotRequired[
        "capo_bedrock_agentcore.types.automation_stream_status.AutomationStreamStatus"
    ]
    """<p>The status of the automation stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationStreamUpdate) -> dict:
    out: dict = {}
    if "stream_status" in value:
        import capo_bedrock_agentcore.types.automation_stream_status

        out["streamStatus"] = (
            capo_bedrock_agentcore.types.automation_stream_status.serialize_json(
                value["stream_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationStreamUpdate:
    out: AutomationStreamUpdate = {}  # type: ignore[typeddict-item]
    if data.get("streamStatus") is not None:
        import capo_bedrock_agentcore.types.automation_stream_status

        out["stream_status"] = (
            capo_bedrock_agentcore.types.automation_stream_status.deserialize_json(
                data["streamStatus"]
            )
        )
    return out
