"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Sources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.source

Sources: TypeAlias = list["capo_observabilityadmin.types.source.Source"]


# --- restJson1 ser/de ---
def serialize_json(value: Sources) -> list:
    import capo_observabilityadmin.types.source

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.source.serialize_json(item))
    return out


def deserialize_json(data: list) -> Sources:
    import capo_observabilityadmin.types.source

    out: Sources = []
    for item in data:
        out.append(capo_observabilityadmin.types.source.deserialize_json(item))
    return out
