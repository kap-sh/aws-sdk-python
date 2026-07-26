"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_set_properties

ImageSetPropertiesList: TypeAlias = list[
    "capo_medical_imaging.types.image_set_properties.ImageSetProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetPropertiesList) -> list:
    import capo_medical_imaging.types.image_set_properties

    out: list = []
    for item in value:
        out.append(capo_medical_imaging.types.image_set_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageSetPropertiesList:
    import capo_medical_imaging.types.image_set_properties

    out: ImageSetPropertiesList = []
    for item in data:
        out.append(
            capo_medical_imaging.types.image_set_properties.deserialize_json(item)
        )
    return out
