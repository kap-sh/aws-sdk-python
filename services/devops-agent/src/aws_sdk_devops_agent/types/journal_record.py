"""Generated from Smithy shape ``com.amazonaws.devopsagent#JournalRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.journal_timestamp
    import aws_sdk_devops_agent.types.user_reference


class JournalRecord(TypedDict):
    agent_space_id: "str"
    """<p>The unique identifier for the agent space containing this record</p>"""
    execution_id: "str"
    """<p>The execution ID associated with this journal record</p>"""
    record_id: "str"
    """<p>The unique identifier for this journal record</p>"""
    content: "object"
    """<p>The content of this journal record</p>"""
    created_at: "aws_sdk_devops_agent.types.journal_timestamp.JournalTimestamp"
    """<p>Timestamp when this journal record was created</p>"""
    record_type: "str"
    """<p>The type of this journal record</p>"""
    user_reference: NotRequired[
        "aws_sdk_devops_agent.types.user_reference.UserReference"
    ]
    """<p>Reference to the user associated with this journal record</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JournalRecord) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["executionId"] = value["execution_id"]
    out["recordId"] = value["record_id"]
    out["content"] = value["content"]
    import aws_sdk_devops_agent.types.journal_timestamp

    out["createdAt"] = aws_sdk_devops_agent.types.journal_timestamp.serialize_json(
        value["created_at"]
    )
    out["recordType"] = value["record_type"]
    if "user_reference" in value:
        import aws_sdk_devops_agent.types.user_reference

        out["userReference"] = aws_sdk_devops_agent.types.user_reference.serialize_json(
            value["user_reference"]
        )
    return out


def deserialize_json(data: dict) -> JournalRecord:
    out: JournalRecord = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("JournalRecord.agent_space_id required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("JournalRecord.execution_id required")
    if "recordId" in data:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError("JournalRecord.record_id required")
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("JournalRecord.content required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types.journal_timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types.journal_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("JournalRecord.created_at required")
    if "recordType" in data:
        out["record_type"] = data["recordType"]
    else:
        raise DeserializationError("JournalRecord.record_type required")
    if "userReference" in data:
        import aws_sdk_devops_agent.types.user_reference

        out["user_reference"] = (
            aws_sdk_devops_agent.types.user_reference.deserialize_json(
                data["userReference"]
            )
        )
    return out
