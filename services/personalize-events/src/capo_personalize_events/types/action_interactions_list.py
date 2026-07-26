"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ActionInteractionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.action_interaction

ActionInteractionsList: TypeAlias = list[
    "capo_personalize_events.types.action_interaction.ActionInteraction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionInteractionsList) -> list:
    import capo_personalize_events.types.action_interaction

    out: list = []
    for item in value:
        out.append(
            capo_personalize_events.types.action_interaction.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ActionInteractionsList:
    import capo_personalize_events.types.action_interaction

    out: ActionInteractionsList = []
    for item in data:
        out.append(
            capo_personalize_events.types.action_interaction.deserialize_json(item)
        )
    return out
