"""Generated from Smithy shape ``com.amazonaws.devopsagent#ChatExecution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.resource_id


class ChatExecution(TypedDict):
    execution_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for the execution</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the chat was created</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>Timestamp when the chat was last updated</p>"""
    summary: NotRequired["str"]
    """<p>Summary or title of the chat</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatExecution) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    return out


def deserialize_json(data: dict) -> ChatExecution:
    out: ChatExecution = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("ChatExecution.execution_id required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ChatExecution.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "summary" in data:
        out["summary"] = data["summary"]
    return out
