"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_output

MemoryRecordsOutputList: TypeAlias = list[
    "capo_bedrock_agentcore.types.memory_record_output.MemoryRecordOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordsOutputList) -> list:
    import capo_bedrock_agentcore.types.memory_record_output

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.memory_record_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryRecordsOutputList:
    import capo_bedrock_agentcore.types.memory_record_output

    out: MemoryRecordsOutputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.memory_record_output.deserialize_json(item)
        )
    return out
