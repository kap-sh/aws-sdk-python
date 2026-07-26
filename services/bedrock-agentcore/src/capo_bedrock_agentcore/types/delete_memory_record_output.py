"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteMemoryRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_id


class DeleteMemoryRecordOutput(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The identifier of the memory record that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryRecordOutput) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    return out


def deserialize_json(data: dict) -> DeleteMemoryRecordOutput:
    out: DeleteMemoryRecordOutput = {}  # type: ignore[typeddict-item]
    if "memoryRecordId" in data:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        raise DeserializationError("DeleteMemoryRecordOutput.memory_record_id required")
    return out
