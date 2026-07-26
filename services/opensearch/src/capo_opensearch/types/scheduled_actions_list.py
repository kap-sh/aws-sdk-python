"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.scheduled_action

ScheduledActionsList: TypeAlias = list[
    "capo_opensearch.types.scheduled_action.ScheduledAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledActionsList) -> list:
    import capo_opensearch.types.scheduled_action

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.scheduled_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduledActionsList:
    import capo_opensearch.types.scheduled_action

    out: ScheduledActionsList = []
    for item in data:
        out.append(capo_opensearch.types.scheduled_action.deserialize_json(item))
    return out
