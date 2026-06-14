"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Memory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.arn
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.indexed_keys_list
    import aws_sdk_bedrock_agentcore_control.types.memory_arn
    import aws_sdk_bedrock_agentcore_control.types.memory_id
    import aws_sdk_bedrock_agentcore_control.types.memory_status
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_list
    import aws_sdk_bedrock_agentcore_control.types.name
    import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources


class Memory(TypedDict):
    arn: "aws_sdk_bedrock_agentcore_control.types.memory_arn.MemoryArn"
    """<p>The Amazon Resource Name (ARN) of the memory.</p>"""
    id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.name.Name"
    """<p>The name of the memory.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the memory.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.arn.Arn"]
    """<p>The ARN of the KMS key used to encrypt the memory.</p>"""
    memory_execution_role_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
    ]
    """<p>The ARN of the IAM role that provides permissions for the memory.</p>"""
    event_expiry_duration: "int"
    """<p>The number of days after which memory events will expire.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.memory_status.MemoryStatus"
    """<p>The current status of the memory.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the memory is in a failed state.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the memory was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the memory was last updated.</p>"""
    strategies: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.memory_strategy_list.MemoryStrategyList"
    ]
    """<p>The list of memory strategies associated with this memory.</p>"""
    indexed_keys: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
    ]
    """<p>The indexed metadata keys for this memory. Only indexed keys can be used in metadata filters.</p>"""
    stream_delivery_resources: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
    ]
    """<p>Configuration for streaming memory record data to external resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Memory) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "memory_execution_role_arn" in value:
        out["memoryExecutionRoleArn"] = value["memory_execution_role_arn"]
    out["eventExpiryDuration"] = value["event_expiry_duration"]
    import aws_sdk_bedrock_agentcore_control.types.memory_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.memory_status.serialize_json(
            value["status"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "strategies" in value:
        import aws_sdk_bedrock_agentcore_control.types.memory_strategy_list

        out["strategies"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_list.serialize_json(
                value["strategies"]
            )
        )
    if "indexed_keys" in value:
        import aws_sdk_bedrock_agentcore_control.types.indexed_keys_list

        out["indexedKeys"] = (
            aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.serialize_json(
                value["indexed_keys"]
            )
        )
    if "stream_delivery_resources" in value:
        import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources

        out["streamDeliveryResources"] = (
            aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.serialize_json(
                value["stream_delivery_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> Memory:
    out: Memory = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Memory.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Memory.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Memory.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "memoryExecutionRoleArn" in data:
        out["memory_execution_role_arn"] = data["memoryExecutionRoleArn"]
    if "eventExpiryDuration" in data:
        out["event_expiry_duration"] = data["eventExpiryDuration"]
    else:
        raise DeserializationError("Memory.event_expiry_duration required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("Memory.status required")
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Memory.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Memory.updated_at required")
    if "strategies" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory_strategy_list

        out["strategies"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_list.deserialize_json(
                data["strategies"]
            )
        )
    if "indexedKeys" in data:
        import aws_sdk_bedrock_agentcore_control.types.indexed_keys_list

        out["indexed_keys"] = (
            aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.deserialize_json(
                data["indexedKeys"]
            )
        )
    if "streamDeliveryResources" in data:
        import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources

        out["stream_delivery_resources"] = (
            aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.deserialize_json(
                data["streamDeliveryResources"]
            )
        )
    return out
