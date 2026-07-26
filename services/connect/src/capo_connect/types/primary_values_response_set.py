"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryValuesResponseSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.primary_value_response

PrimaryValuesResponseSet: TypeAlias = list[
    "capo_connect.types.primary_value_response.PrimaryValueResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValuesResponseSet) -> list:
    import capo_connect.types.primary_value_response

    out: list = []
    for item in value:
        out.append(capo_connect.types.primary_value_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrimaryValuesResponseSet:
    import capo_connect.types.primary_value_response

    out: PrimaryValuesResponseSet = []
    for item in data:
        out.append(capo_connect.types.primary_value_response.deserialize_json(item))
    return out
