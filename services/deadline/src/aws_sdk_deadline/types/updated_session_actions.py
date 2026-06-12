"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedSessionActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.session_action_id
    import aws_sdk_deadline.types.updated_session_action_info

UpdatedSessionActions: TypeAlias = dict[
    "aws_sdk_deadline.types.session_action_id.SessionActionId",
    "aws_sdk_deadline.types.updated_session_action_info.UpdatedSessionActionInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdatedSessionActions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_deadline.types.updated_session_action_info

        out[key] = aws_sdk_deadline.types.updated_session_action_info.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> UpdatedSessionActions:
    out: UpdatedSessionActions = {}
    for key, value in data.items():
        import aws_sdk_deadline.types.updated_session_action_info

        out[key] = aws_sdk_deadline.types.updated_session_action_info.deserialize_json(
            value
        )
    return out
