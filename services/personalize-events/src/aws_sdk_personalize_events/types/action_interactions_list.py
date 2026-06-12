"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ActionInteractionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.action_interaction

ActionInteractionsList: TypeAlias = list[
    "aws_sdk_personalize_events.types.action_interaction.ActionInteraction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionInteractionsList) -> list:
    import aws_sdk_personalize_events.types.action_interaction

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize_events.types.action_interaction.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ActionInteractionsList:
    import aws_sdk_personalize_events.types.action_interaction

    out: ActionInteractionsList = []
    for item in data:
        out.append(
            aws_sdk_personalize_events.types.action_interaction.deserialize_json(item)
        )
    return out
