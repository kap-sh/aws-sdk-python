"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceTypeValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.resource_type_values

ResourceTypeValuesList: TypeAlias = list[
    "capo_dlm.types.resource_type_values.ResourceTypeValues"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeValuesList) -> list:
    import capo_dlm.types.resource_type_values

    out: list = []
    for item in value:
        out.append(capo_dlm.types.resource_type_values.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTypeValuesList:
    import capo_dlm.types.resource_type_values

    out: ResourceTypeValuesList = []
    for item in data:
        out.append(capo_dlm.types.resource_type_values.deserialize_json(item))
    return out
