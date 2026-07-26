"""Generated from Smithy shape ``com.amazonaws.ram#PolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.policy

PolicyList: TypeAlias = list["capo_ram.types.policy.Policy"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyList) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyList:
    return list(data)
