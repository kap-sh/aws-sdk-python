"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.memory_content
    import aws_sdk_bedrock_agentcore.types.memory_record_id
    import aws_sdk_bedrock_agentcore.types.memory_record_metadata_map
    import aws_sdk_bedrock_agentcore.types.memory_strategy_id
    import aws_sdk_bedrock_agentcore.types.namespaces_list


class MemoryRecordSummary(TypedDict):
    memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique identifier of the memory record.</p>"""
    content: "aws_sdk_bedrock_agentcore.types.memory_content.MemoryContent"
    """<p>The content of the memory record.</p>"""
    memory_strategy_id: (
        "aws_sdk_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    )
    """<p>The identifier of the memory strategy associated with this record.</p>"""
    namespaces: "aws_sdk_bedrock_agentcore.types.namespaces_list.NamespacesList"
    """<p>The namespaces associated with this memory record.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the memory record was created.</p>"""
    score: NotRequired["float"]
    """<p>The relevance score of the memory record when returned as part of a search result. Higher values indicate greater relevance to the search query.</p>"""
    metadata: NotRequired[
        "aws_sdk_bedrock_agentcore.types.memory_record_metadata_map.MemoryRecordMetadataMap"
    ]
    """<p>A map of metadata key-value pairs associated with a memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordSummary) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    import aws_sdk_bedrock_agentcore.types.memory_content

    out["content"] = aws_sdk_bedrock_agentcore.types.memory_content.serialize_json(
        value["content"]
    )
    out["memoryStrategyId"] = value["memory_strategy_id"]
    import aws_sdk_bedrock_agentcore.types.namespaces_list

    out["namespaces"] = aws_sdk_bedrock_agentcore.types.namespaces_list.serialize_json(
        value["namespaces"]
    )
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "score" in value:
        out["score"] = value["score"]
    if "metadata" in value:
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordSummary:
    out: MemoryRecordSummary = {}  # type: ignore[typeddict-item]
    if "memoryRecordId" in data:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        raise DeserializationError("MemoryRecordSummary.memory_record_id required")
    if "content" in data:
        import aws_sdk_bedrock_agentcore.types.memory_content

        out["content"] = (
            aws_sdk_bedrock_agentcore.types.memory_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordSummary.content required")
    if "memoryStrategyId" in data:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    else:
        raise DeserializationError("MemoryRecordSummary.memory_strategy_id required")
    if "namespaces" in data:
        import aws_sdk_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = (
            aws_sdk_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordSummary.namespaces required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordSummary.created_at required")
    if "score" in data:
        out["score"] = data["score"]
    if "metadata" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_metadata_map.deserialize_json(
                data["metadata"]
            )
        )
    return out
