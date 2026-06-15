"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseClickResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_action_status


class MouseClickResult(TypedDict):
    status: "aws_sdk_bedrock_agentcore.types.browser_action_status.BrowserActionStatus"
    """<p>The status of the action execution.</p>"""
    error: NotRequired["str"]
    """<p>The error message. Present only when the action failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseClickResult) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.browser_action_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.browser_action_status.serialize_json(
            value["status"]
        )
    )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> MouseClickResult:
    out: MouseClickResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.browser_action_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.browser_action_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("MouseClickResult.status required")
    if "error" in data:
        out["error"] = data["error"]
    return out
