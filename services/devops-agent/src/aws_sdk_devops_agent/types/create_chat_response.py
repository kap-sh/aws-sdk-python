"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateChatResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.resource_id


class CreateChatResponse(TypedDict):
    execution_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for the created execution</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the chat was created</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateChatResponse:
    out: CreateChatResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("CreateChatResponse.execution_id required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateChatResponse.created_at required")
    return out
