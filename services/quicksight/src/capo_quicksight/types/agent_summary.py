"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_description
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_name
    import capo_quicksight.types.icon_id


class AgentSummary(TypedDict, closed=True):
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    name: "capo_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    description: NotRequired["capo_quicksight.types.agent_description.AgentDescription"]
    """<p>A description of the agent.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the agent was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time that the agent was last updated.</p>"""
    icon_id: NotRequired["capo_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_quicksight.types._prelude.timestamp

    out["CreatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_quicksight.types._prelude.timestamp

    out["UpdatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
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
        import capo_quicksight.types._prelude.timestamp

        out["created_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("AgentSummary.created_at required")
    if "UpdatedAt" in data:
        import capo_quicksight.types._prelude.timestamp

        out["updated_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("AgentSummary.updated_at required")
    if "IconId" in data:
        out["icon_id"] = data["IconId"]
    return out
