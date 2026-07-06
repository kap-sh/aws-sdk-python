"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.event


class CreateEventOutput(TypedDict, closed=True):
    event: "aws_sdk_bedrock_agentcore.types.event.Event"
    """<p>The event that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.event

    out["event"] = aws_sdk_bedrock_agentcore.types.event.serialize_json(value["event"])
    return out


def deserialize_json(data: dict) -> CreateEventOutput:
    out: CreateEventOutput = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import aws_sdk_bedrock_agentcore.types.event

        out["event"] = aws_sdk_bedrock_agentcore.types.event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("CreateEventOutput.event required")
    return out
