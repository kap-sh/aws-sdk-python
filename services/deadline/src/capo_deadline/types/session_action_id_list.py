"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.session_action_id

SessionActionIdList: TypeAlias = list[
    "capo_deadline.types.session_action_id.SessionActionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SessionActionIdList:
    return list(data)
