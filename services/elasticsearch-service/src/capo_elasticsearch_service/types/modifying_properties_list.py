"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ModifyingPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.modifying_properties

ModifyingPropertiesList: TypeAlias = list[
    "capo_elasticsearch_service.types.modifying_properties.ModifyingProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModifyingPropertiesList) -> list:
    import capo_elasticsearch_service.types.modifying_properties

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.modifying_properties.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ModifyingPropertiesList:
    import capo_elasticsearch_service.types.modifying_properties

    out: ModifyingPropertiesList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.modifying_properties.deserialize_json(item)
        )
    return out
