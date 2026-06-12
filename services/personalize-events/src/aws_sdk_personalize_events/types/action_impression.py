"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ActionImpression``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.action_id

ActionImpression: TypeAlias = list[
    "aws_sdk_personalize_events.types.action_id.ActionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionImpression) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionImpression:
    return list(data)
