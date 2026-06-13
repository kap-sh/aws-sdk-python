"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.event

EventList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: EventList) -> list:
    import aws_sdk_bedrock_agentcore.types.event
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventList:
    import aws_sdk_bedrock_agentcore.types.event
    out: EventList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.event.deserialize_json(item))
    return out