"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateMemoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.arn
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.indexed_keys_list
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list
    import aws_sdk_bedrock_agentcore_control.types.name
    import aws_sdk_bedrock_agentcore_control.types.non_empty_string
    import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources
    import aws_sdk_bedrock_agentcore_control.types.tags_map


class CreateMemoryInput(TypedDict):
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.name.Name"
    """<p>The name of the memory. The name must be unique within your account.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the memory.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>"""
    memory_execution_role_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>"""
    event_expiry_duration: "int"
    """<p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>"""
    memory_strategies: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
    ]
    """<p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>"""
    indexed_keys: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
    ]
    """<p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>"""
    stream_delivery_resources: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
    ]
    """<p>Configuration for streaming memory record data to external resources.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemoryInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "memory_execution_role_arn" in value:
        out["memoryExecutionRoleArn"] = value["memory_execution_role_arn"]
    out["eventExpiryDuration"] = value["event_expiry_duration"]
    if "memory_strategies" in value:
        import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list

        out["memoryStrategies"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.serialize_json(
                value["memory_strategies"]
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
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMemoryInput:
    out: CreateMemoryInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMemoryInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "memoryExecutionRoleArn" in data:
        out["memory_execution_role_arn"] = data["memoryExecutionRoleArn"]
    if "eventExpiryDuration" in data:
        out["event_expiry_duration"] = data["eventExpiryDuration"]
    else:
        raise DeserializationError("CreateMemoryInput.event_expiry_duration required")
    if "memoryStrategies" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list

        out["memory_strategies"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.deserialize_json(
                data["memoryStrategies"]
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
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
