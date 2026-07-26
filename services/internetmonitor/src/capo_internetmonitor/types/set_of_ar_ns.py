"""Generated from Smithy shape ``com.amazonaws.internetmonitor#SetOfARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_internetmonitor.types.arn

SetOfARNs: TypeAlias = list["capo_internetmonitor.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: SetOfARNs) -> list:
    return list(value)


def deserialize_json(data: list) -> SetOfARNs:
    return list(data)
