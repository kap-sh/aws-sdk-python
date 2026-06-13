"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateEventInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.actor_id
    import aws_sdk_bedrock_agentcore.types.branch
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.metadata_map
    import aws_sdk_bedrock_agentcore.types.payload_type_list
    import aws_sdk_bedrock_agentcore.types.session_id
    import datetime

class CreateEventInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource in which to create the event.</p>"""
    actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>"""
    session_id: NotRequired["aws_sdk_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>"""
    event_timestamp: "datetime.datetime"
    """<p>The timestamp when the event occurred. If not specified, the current time is used.</p>"""
    payload: "aws_sdk_bedrock_agentcore.types.payload_type_list.PayloadTypeList"
    """<p>The content payload of the event. This can include conversational data or binary content.</p>"""
    branch: NotRequired["aws_sdk_bedrock_agentcore.types.branch.Branch"]
    """<p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agentcore.types.metadata_map.MetadataMap"]
    """<p>The key-value metadata to attach to the event.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateEventInput) -> dict:
    out: dict = {}
    out["actorId"] = value["actor_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp
    out["eventTimestamp"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(value["event_timestamp"])
    import aws_sdk_bedrock_agentcore.types.payload_type_list
    out["payload"] = aws_sdk_bedrock_agentcore.types.payload_type_list.serialize_json(value["payload"])
    if "branch" in value:
        import aws_sdk_bedrock_agentcore.types.branch
        out["branch"] = aws_sdk_bedrock_agentcore.types.branch.serialize_json(value["branch"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "metadata" in value:
        import aws_sdk_bedrock_agentcore.types.metadata_map
        out["metadata"] = aws_sdk_bedrock_agentcore.types.metadata_map.serialize_json(value["metadata"])
    return out


def deserialize_json(data: dict) -> CreateEventInput:
    out: CreateEventInput = {}  # type: ignore[typeddict-item]
    if "actorId" in data:
        out["actor_id"] = data["actorId"]
    else:
        raise DeserializationError("CreateEventInput.actor_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "eventTimestamp" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp
        out["event_timestamp"] = aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(data["eventTimestamp"])
    else:
        raise DeserializationError("CreateEventInput.event_timestamp required")
    if "payload" in data:
        import aws_sdk_bedrock_agentcore.types.payload_type_list
        out["payload"] = aws_sdk_bedrock_agentcore.types.payload_type_list.deserialize_json(data["payload"])
    else:
        raise DeserializationError("CreateEventInput.payload required")
    if "branch" in data:
        import aws_sdk_bedrock_agentcore.types.branch
        out["branch"] = aws_sdk_bedrock_agentcore.types.branch.deserialize_json(data["branch"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "metadata" in data:
        import aws_sdk_bedrock_agentcore.types.metadata_map
        out["metadata"] = aws_sdk_bedrock_agentcore.types.metadata_map.deserialize_json(data["metadata"])
    return out