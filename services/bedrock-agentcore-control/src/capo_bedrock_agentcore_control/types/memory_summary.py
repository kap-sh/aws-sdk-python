"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemorySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.memory_arn
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.memory_status


class MemorySummary(TypedDict, closed=True):
    arn: NotRequired["capo_bedrock_agentcore_control.types.memory_arn.MemoryArn"]
    """<p>The Amazon Resource Name (ARN) of the memory.</p>"""
    id: NotRequired["capo_bedrock_agentcore_control.types.memory_id.MemoryId"]
    """<p>The unique identifier of the memory.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore_control.types.memory_status.MemoryStatus"
    ]
    """<p>The current status of the memory.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the memory was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the memory was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemorySummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        import capo_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.memory_status.serialize_json(
                value["status"]
            )
        )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> MemorySummary:
    out: MemorySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        import capo_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.memory_status.deserialize_json(
                data["status"]
            )
        )
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("MemorySummary.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("MemorySummary.updated_at required")
    return out
