"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.reserved_instance

ReservedInstanceList: TypeAlias = list[
    "capo_opensearch.types.reserved_instance.ReservedInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedInstanceList) -> list:
    import capo_opensearch.types.reserved_instance

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.reserved_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReservedInstanceList:
    import capo_opensearch.types.reserved_instance

    out: ReservedInstanceList = []
    for item in data:
        out.append(capo_opensearch.types.reserved_instance.deserialize_json(item))
    return out
