"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResponseChunk``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.content_delta_event
    import aws_sdk_bedrock_agentcore.types.content_start_event
    import aws_sdk_bedrock_agentcore.types.content_stop_event


class ResponseChunk(TypedDict):
    content_start: NotRequired[
        "aws_sdk_bedrock_agentcore.types.content_start_event.ContentStartEvent"
    ]
    """<p>An event indicating the start of content streaming from the command execution. This is the first chunk received.</p>"""
    content_delta: NotRequired[
        "aws_sdk_bedrock_agentcore.types.content_delta_event.ContentDeltaEvent"
    ]
    """<p>An event containing incremental output (stdout or stderr) from the command execution. These are the middle chunks.</p>"""
    content_stop: NotRequired[
        "aws_sdk_bedrock_agentcore.types.content_stop_event.ContentStopEvent"
    ]
    """<p>An event indicating the completion of the command execution, including the exit code and final status. This is the last chunk received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseChunk) -> dict:
    out: dict = {}
    if "content_start" in value:
        import aws_sdk_bedrock_agentcore.types.content_start_event

        out["contentStart"] = (
            aws_sdk_bedrock_agentcore.types.content_start_event.serialize_json(
                value["content_start"]
            )
        )
    if "content_delta" in value:
        import aws_sdk_bedrock_agentcore.types.content_delta_event

        out["contentDelta"] = (
            aws_sdk_bedrock_agentcore.types.content_delta_event.serialize_json(
                value["content_delta"]
            )
        )
    if "content_stop" in value:
        import aws_sdk_bedrock_agentcore.types.content_stop_event

        out["contentStop"] = (
            aws_sdk_bedrock_agentcore.types.content_stop_event.serialize_json(
                value["content_stop"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseChunk:
    out: ResponseChunk = {}  # type: ignore[typeddict-item]
    if "contentStart" in data:
        import aws_sdk_bedrock_agentcore.types.content_start_event

        out["content_start"] = (
            aws_sdk_bedrock_agentcore.types.content_start_event.deserialize_json(
                data["contentStart"]
            )
        )
    if "contentDelta" in data:
        import aws_sdk_bedrock_agentcore.types.content_delta_event

        out["content_delta"] = (
            aws_sdk_bedrock_agentcore.types.content_delta_event.deserialize_json(
                data["contentDelta"]
            )
        )
    if "contentStop" in data:
        import aws_sdk_bedrock_agentcore.types.content_stop_event

        out["content_stop"] = (
            aws_sdk_bedrock_agentcore.types.content_stop_event.deserialize_json(
                data["contentStop"]
            )
        )
    return out
