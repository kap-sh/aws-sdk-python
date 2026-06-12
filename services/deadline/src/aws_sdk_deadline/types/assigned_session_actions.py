"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.assigned_session_action

AssignedSessionActions: TypeAlias = list[
    "aws_sdk_deadline.types.assigned_session_action.AssignedSessionAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionActions) -> list:
    import aws_sdk_deadline.types.assigned_session_action

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.assigned_session_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssignedSessionActions:
    import aws_sdk_deadline.types.assigned_session_action

    out: AssignedSessionActions = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.assigned_session_action.deserialize_json(item)
        )
    return out
