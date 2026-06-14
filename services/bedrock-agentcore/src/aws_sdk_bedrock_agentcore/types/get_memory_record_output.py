"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetMemoryRecordOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record


class GetMemoryRecordOutput(TypedDict):
    memory_record: "aws_sdk_bedrock_agentcore.types.memory_record.MemoryRecord"
    """<p>The requested memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryRecordOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_record

    out["memoryRecord"] = aws_sdk_bedrock_agentcore.types.memory_record.serialize_json(
        value["memory_record"]
    )
    return out


def deserialize_json(data: dict) -> GetMemoryRecordOutput:
    out: GetMemoryRecordOutput = {}  # type: ignore[typeddict-item]
    if "memoryRecord" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record

        out["memory_record"] = (
            aws_sdk_bedrock_agentcore.types.memory_record.deserialize_json(
                data["memoryRecord"]
            )
        )
    else:
        raise DeserializationError("GetMemoryRecordOutput.memory_record required")
    return out
