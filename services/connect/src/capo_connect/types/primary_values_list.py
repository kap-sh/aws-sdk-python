"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.record_primary_value

PrimaryValuesList: TypeAlias = list[
    "capo_connect.types.record_primary_value.RecordPrimaryValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValuesList) -> list:
    import capo_connect.types.record_primary_value

    out: list = []
    for item in value:
        out.append(capo_connect.types.record_primary_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrimaryValuesList:
    import capo_connect.types.record_primary_value

    out: PrimaryValuesList = []
    for item in data:
        out.append(capo_connect.types.record_primary_value.deserialize_json(item))
    return out
