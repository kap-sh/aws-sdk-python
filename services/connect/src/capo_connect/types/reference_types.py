"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.reference_type

ReferenceTypes: TypeAlias = list["capo_connect.types.reference_type.ReferenceType"]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceTypes) -> list:
    import capo_connect.types.reference_type

    out: list = []
    for item in value:
        out.append(capo_connect.types.reference_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceTypes:
    import capo_connect.types.reference_type

    out: ReferenceTypes = []
    for item in data:
        out.append(capo_connect.types.reference_type.deserialize_json(item))
    return out
