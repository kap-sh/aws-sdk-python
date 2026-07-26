"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfColorCorrection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.color_correction

__listOfColorCorrection: TypeAlias = list[
    "capo_medialive.types.color_correction.ColorCorrection"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfColorCorrection) -> list:
    import capo_medialive.types.color_correction

    out: list = []
    for item in value:
        out.append(capo_medialive.types.color_correction.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfColorCorrection:
    import capo_medialive.types.color_correction

    out: __listOfColorCorrection = []
    for item in data:
        out.append(capo_medialive.types.color_correction.deserialize_json(item))
    return out
