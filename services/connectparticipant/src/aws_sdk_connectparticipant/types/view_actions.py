"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ViewActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.view_action

ViewActions: TypeAlias = list["aws_sdk_connectparticipant.types.view_action.ViewAction"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewActions) -> list:
    return list(value)


def deserialize_json(data: list) -> ViewActions:
    return list(data)
