"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.agent_arn
    import aws_sdk_quicksight.types.agent_description
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.agent_name
    import aws_sdk_quicksight.types.icon_id


class AgentSummary(TypedDict):
    arn: "aws_sdk_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    name: "aws_sdk_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.agent_description.AgentDescription"
    ]
    """<p>A description of the agent.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the agent was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time that the agent was last updated.</p>"""
    icon_id: NotRequired["aws_sdk_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_quicksight.types._prelude.timestamp

    out["CreatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_quicksight.types._prelude.timestamp

    out["UpdatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "icon_id" in value:
        out["IconId"] = value["icon_id"]
    return out


def deserialize_json(data: dict) -> AgentSummary:
    out: AgentSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("AgentSummary.arn required")
    if "AgentId" in data:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("AgentSummary.agent_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AgentSummary.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("AgentSummary.created_at required")
    if "UpdatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("AgentSummary.updated_at required")
    if "IconId" in data:
        out["icon_id"] = data["IconId"]
    return out
