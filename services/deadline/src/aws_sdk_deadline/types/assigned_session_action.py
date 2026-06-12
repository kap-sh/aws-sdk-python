"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.assigned_session_action_definition
    import aws_sdk_deadline.types.session_action_id


class AssignedSessionAction(TypedDict):
    session_action_id: "aws_sdk_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID for the assigned session.</p>"""
    definition: "aws_sdk_deadline.types.assigned_session_action_definition.AssignedSessionActionDefinition"
    """<p>The definition of the assigned session action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionAction) -> dict:
    out: dict = {}
    out["sessionActionId"] = value["session_action_id"]
    import aws_sdk_deadline.types.assigned_session_action_definition

    out["definition"] = (
        aws_sdk_deadline.types.assigned_session_action_definition.serialize_json(
            value["definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssignedSessionAction:
    out: AssignedSessionAction = {}  # type: ignore[typeddict-item]
    if "sessionActionId" in data:
        out["session_action_id"] = data["sessionActionId"]
    else:
        raise DeserializationError("AssignedSessionAction.session_action_id required")
    if "definition" in data:
        import aws_sdk_deadline.types.assigned_session_action_definition

        out["definition"] = (
            aws_sdk_deadline.types.assigned_session_action_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("AssignedSessionAction.definition required")
    return out
