"""Generated from Smithy shape ``com.amazonaws.deadline#ManifestPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.manifest_properties

ManifestPropertiesList: TypeAlias = list[
    "capo_deadline.types.manifest_properties.ManifestProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManifestPropertiesList) -> list:
    import capo_deadline.types.manifest_properties

    out: list = []
    for item in value:
        out.append(capo_deadline.types.manifest_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> ManifestPropertiesList:
    import capo_deadline.types.manifest_properties

    out: ManifestPropertiesList = []
    for item in data:
        out.append(capo_deadline.types.manifest_properties.deserialize_json(item))
    return out
