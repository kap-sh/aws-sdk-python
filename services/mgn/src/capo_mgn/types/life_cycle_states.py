"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.life_cycle_state

LifeCycleStates: TypeAlias = list["capo_mgn.types.life_cycle_state.LifeCycleState"]


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleStates) -> list:
    return list(value)


def deserialize_json(data: list) -> LifeCycleStates:
    return list(data)
