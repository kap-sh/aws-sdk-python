"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordCreateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.memory_content
    import aws_sdk_bedrock_agentcore.types.memory_record_metadata_map
    import aws_sdk_bedrock_agentcore.types.memory_strategy_id
    import aws_sdk_bedrock_agentcore.types.namespaces_list
    import aws_sdk_bedrock_agentcore.types.request_identifier


class MemoryRecordCreateInput(TypedDict, closed=True):
    request_identifier: (
        "aws_sdk_bedrock_agentcore.types.request_identifier.RequestIdentifier"
    )
    """<p>A client-provided identifier for tracking this specific record creation request.</p>"""
    namespaces: "aws_sdk_bedrock_agentcore.types.namespaces_list.NamespacesList"
    """<p>A list of namespace identifiers that categorize or group the memory record.</p>"""
    content: "aws_sdk_bedrock_agentcore.types.memory_content.MemoryContent"
    """<p>The content to be stored within the memory record.</p>"""
    timestamp: "datetime.datetime"
    """<p>Time at which the memory record was created.</p>"""
    memory_strategy_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The ID of the memory strategy that defines how this memory record is grouped.</p>"""
    metadata: NotRequired[
        "aws_sdk_bedrock_agentcore.types.memory_record_metadata_map.MemoryRecordMetadataMap"
    ]
    """<p>Metadata key-value pairs to be stored with the memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordCreateInput) -> dict:
    out: dict = {}
    out["requestIdentifier"] = value["request_identifier"]
    import aws_sdk_bedrock_agentcore.types.namespaces_list

    out["namespaces"] = aws_sdk_bedrock_agentcore.types.namespaces_list.serialize_json(
        value["namespaces"]
    )
    import aws_sdk_bedrock_agentcore.types.memory_content

    out["content"] = aws_sdk_bedrock_agentcore.types.memory_content.serialize_json(
        value["content"]
    )
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp

    out["timestamp"] = (
        aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    )
    if "memory_strategy_id" in value:
        out["memoryStrategyId"] = value["memory_strategy_id"]
    if "metadata" in value:
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordCreateInput:
    out: MemoryRecordCreateInput = {}  # type: ignore[typeddict-item]
    if "requestIdentifier" in data:
        out["request_identifier"] = data["requestIdentifier"]
    else:
        raise DeserializationError(
            "MemoryRecordCreateInput.request_identifier required"
        )
    if "namespaces" in data:
        import aws_sdk_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = (
            aws_sdk_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordCreateInput.namespaces required")
    if "content" in data:
        import aws_sdk_bedrock_agentcore.types.memory_content

        out["content"] = (
            aws_sdk_bedrock_agentcore.types.memory_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordCreateInput.content required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordCreateInput.timestamp required")
    if "memoryStrategyId" in data:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    if "metadata" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_metadata_map.deserialize_json(
                data["metadata"]
            )
        )
    return out
