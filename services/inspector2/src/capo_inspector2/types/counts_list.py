"""Generated from Smithy shape ``com.amazonaws.inspector2#CountsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.counts

CountsList: TypeAlias = list["capo_inspector2.types.counts.Counts"]


# --- restJson1 ser/de ---
def serialize_json(value: CountsList) -> list:
    import capo_inspector2.types.counts

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.counts.serialize_json(item))
    return out


def deserialize_json(data: list) -> CountsList:
    import capo_inspector2.types.counts

    out: CountsList = []
    for item in data:
        out.append(capo_inspector2.types.counts.deserialize_json(item))
    return out
