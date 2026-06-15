"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.target_description
    import aws_sdk_bedrock_agentcore_control.types.target_id
    import aws_sdk_bedrock_agentcore_control.types.target_name
    import aws_sdk_bedrock_agentcore_control.types.target_resource_priority
    import aws_sdk_bedrock_agentcore_control.types.target_status


class TargetSummary(TypedDict):
    target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the target.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the target.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.target_status.TargetStatus"
    """<p>The current status of the target.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The description of the target.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the target was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the target was last updated.</p>"""
    resource_priority: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_resource_priority.TargetResourcePriority"
    ]
    """<p>Priority for resolving resource URI conflicts across targets. Lower values take precedence. Defaults to 1000 when not set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    out["targetId"] = value["target_id"]
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.target_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.target_status.serialize_json(
            value["status"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "resource_priority" in value:
        out["resourcePriority"] = value["resource_priority"]
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("TargetSummary.target_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TargetSummary.name required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.target_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.target_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("TargetSummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("TargetSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("TargetSummary.updated_at required")
    if "resourcePriority" in data:
        out["resource_priority"] = data["resourcePriority"]
    return out
