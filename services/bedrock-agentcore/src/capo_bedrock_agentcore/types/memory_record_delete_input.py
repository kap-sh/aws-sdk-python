"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordDeleteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_id


class MemoryRecordDeleteInput(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique ID of the memory record to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordDeleteInput) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    return out


def deserialize_json(data: dict) -> MemoryRecordDeleteInput:
    out: MemoryRecordDeleteInput = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordId") is not None:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        raise DeserializationError("MemoryRecordDeleteInput.memory_record_id required")
    return out
