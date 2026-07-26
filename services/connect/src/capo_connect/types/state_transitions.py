"""Generated from Smithy shape ``com.amazonaws.connect#StateTransitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.state_transition

StateTransitions: TypeAlias = list[
    "capo_connect.types.state_transition.StateTransition"
]


# --- restJson1 ser/de ---
def serialize_json(value: StateTransitions) -> list:
    import capo_connect.types.state_transition

    out: list = []
    for item in value:
        out.append(capo_connect.types.state_transition.serialize_json(item))
    return out


def deserialize_json(data: list) -> StateTransitions:
    import capo_connect.types.state_transition

    out: StateTransitions = []
    for item in data:
        out.append(capo_connect.types.state_transition.deserialize_json(item))
    return out
