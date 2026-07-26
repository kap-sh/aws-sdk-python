"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.record

Records: TypeAlias = list["capo_observabilityadmin.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: Records) -> list:
    import capo_observabilityadmin.types.record

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> Records:
    import capo_observabilityadmin.types.record

    out: Records = []
    for item in data:
        out.append(capo_observabilityadmin.types.record.deserialize_json(item))
    return out
