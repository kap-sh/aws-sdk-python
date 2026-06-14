"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetEventOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.event


class GetEventOutput(TypedDict):
    event: "aws_sdk_bedrock_agentcore.types.event.Event"
    """<p>The requested event information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.event

    out["event"] = aws_sdk_bedrock_agentcore.types.event.serialize_json(value["event"])
    return out


def deserialize_json(data: dict) -> GetEventOutput:
    out: GetEventOutput = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import aws_sdk_bedrock_agentcore.types.event

        out["event"] = aws_sdk_bedrock_agentcore.types.event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("GetEventOutput.event required")
    return out
