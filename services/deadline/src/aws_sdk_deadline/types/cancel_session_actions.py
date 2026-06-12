"""Generated from Smithy shape ``com.amazonaws.deadline#CancelSessionActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.session_action_id_list
    import aws_sdk_deadline.types.session_id

CancelSessionActions: TypeAlias = dict[
    "aws_sdk_deadline.types.session_id.SessionId",
    "aws_sdk_deadline.types.session_action_id_list.SessionActionIdList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CancelSessionActions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_deadline.types.session_action_id_list

        out[key] = aws_sdk_deadline.types.session_action_id_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CancelSessionActions:
    out: CancelSessionActions = {}
    for key, value in data.items():
        import aws_sdk_deadline.types.session_action_id_list

        out[key] = aws_sdk_deadline.types.session_action_id_list.deserialize_json(value)
    return out
