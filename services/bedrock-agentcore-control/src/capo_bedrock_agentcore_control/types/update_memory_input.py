"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateMemoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.arn
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.indexed_keys_list
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.modify_memory_strategies
    import capo_bedrock_agentcore_control.types.non_empty_string
    import capo_bedrock_agentcore_control.types.stream_delivery_resources


class UpdateMemoryInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
    ]
    """<p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>"""
    memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory to update.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The updated description of the AgentCore Memory resource.</p>"""
    event_expiry_duration: NotRequired["int"]
    """<p>The number of days after which memory events will expire, between 7 and 365 days.</p>"""
    memory_execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.arn.Arn"
    ]
    """<p>The ARN of the IAM role that provides permissions for the AgentCore Memory resource.</p>"""
    memory_strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_memory_strategies.ModifyMemoryStrategies"
    ]
    """<p>The memory strategies to add, modify, or delete.</p>"""
    add_indexed_keys: NotRequired[
        "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
    ]
    """<p>Additional metadata keys to index. Previously indexed keys cannot be removed.</p>"""
    stream_delivery_resources: NotRequired[
        "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
    ]
    """<p>Configuration for streaming memory record data to external resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemoryInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "event_expiry_duration" in value:
        out["eventExpiryDuration"] = value["event_expiry_duration"]
    if "memory_execution_role_arn" in value:
        out["memoryExecutionRoleArn"] = value["memory_execution_role_arn"]
    if "memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.modify_memory_strategies

        out["memoryStrategies"] = (
            capo_bedrock_agentcore_control.types.modify_memory_strategies.serialize_json(
                value["memory_strategies"]
            )
        )
    if "add_indexed_keys" in value:
        import capo_bedrock_agentcore_control.types.indexed_keys_list

        out["addIndexedKeys"] = (
            capo_bedrock_agentcore_control.types.indexed_keys_list.serialize_json(
                value["add_indexed_keys"]
            )
        )
    if "stream_delivery_resources" in value:
        import capo_bedrock_agentcore_control.types.stream_delivery_resources

        out["streamDeliveryResources"] = (
            capo_bedrock_agentcore_control.types.stream_delivery_resources.serialize_json(
                value["stream_delivery_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMemoryInput:
    out: UpdateMemoryInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "eventExpiryDuration" in data:
        out["event_expiry_duration"] = data["eventExpiryDuration"]
    if "memoryExecutionRoleArn" in data:
        out["memory_execution_role_arn"] = data["memoryExecutionRoleArn"]
    if "memoryStrategies" in data:
        import capo_bedrock_agentcore_control.types.modify_memory_strategies

        out["memory_strategies"] = (
            capo_bedrock_agentcore_control.types.modify_memory_strategies.deserialize_json(
                data["memoryStrategies"]
            )
        )
    if "addIndexedKeys" in data:
        import capo_bedrock_agentcore_control.types.indexed_keys_list

        out["add_indexed_keys"] = (
            capo_bedrock_agentcore_control.types.indexed_keys_list.deserialize_json(
                data["addIndexedKeys"]
            )
        )
    if "streamDeliveryResources" in data:
        import capo_bedrock_agentcore_control.types.stream_delivery_resources

        out["stream_delivery_resources"] = (
            capo_bedrock_agentcore_control.types.stream_delivery_resources.deserialize_json(
                data["streamDeliveryResources"]
            )
        )
    return out
