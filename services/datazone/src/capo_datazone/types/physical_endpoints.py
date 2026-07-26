"""Generated from Smithy shape ``com.amazonaws.datazone#PhysicalEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.physical_endpoint

PhysicalEndpoints: TypeAlias = list[
    "capo_datazone.types.physical_endpoint.PhysicalEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalEndpoints) -> list:
    import capo_datazone.types.physical_endpoint

    out: list = []
    for item in value:
        out.append(capo_datazone.types.physical_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhysicalEndpoints:
    import capo_datazone.types.physical_endpoint

    out: PhysicalEndpoints = []
    for item in data:
        out.append(capo_datazone.types.physical_endpoint.deserialize_json(item))
    return out
