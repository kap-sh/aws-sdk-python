"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.assigned_session
    import aws_sdk_deadline.types.session_id

AssignedSessions: TypeAlias = dict[
    "aws_sdk_deadline.types.session_id.SessionId",
    "aws_sdk_deadline.types.assigned_session.AssignedSession",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AssignedSessions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_deadline.types.assigned_session

        out[key] = aws_sdk_deadline.types.assigned_session.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AssignedSessions:
    out: AssignedSessions = {}
    for key, value in data.items():
        import aws_sdk_deadline.types.assigned_session

        out[key] = aws_sdk_deadline.types.assigned_session.deserialize_json(value)
    return out
