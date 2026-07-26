"""Generated from Smithy shape ``com.amazonaws.medialive#ColorCorrectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_color_correction


class ColorCorrectionSettings(TypedDict, closed=True):
    global_color_corrections: NotRequired[
        "capo_medialive.types.__list_of_color_correction.__listOfColorCorrection"
    ]
    """An array of colorCorrections that applies when you are using 3D LUT files to perform color conversion on video. Each colorCorrection contains one 3D LUT file (that defines the color mapping for converting an input color space to an output color space), and the input/output combination that this 3D LUT file applies to. MediaLive reads the color space in the input metadata, determines the color space that you have specified for the output, and finds and uses the LUT file that applies to this combination."""


# --- restJson1 ser/de ---
def serialize_json(value: ColorCorrectionSettings) -> dict:
    out: dict = {}
    if "global_color_corrections" in value:
        import capo_medialive.types.__list_of_color_correction

        out["globalColorCorrections"] = (
            capo_medialive.types.__list_of_color_correction.serialize_json(
                value["global_color_corrections"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColorCorrectionSettings:
    out: ColorCorrectionSettings = {}  # type: ignore[typeddict-item]
    if "globalColorCorrections" in data:
        import capo_medialive.types.__list_of_color_correction

        out["global_color_corrections"] = (
            capo_medialive.types.__list_of_color_correction.deserialize_json(
                data["globalColorCorrections"]
            )
        )
    return out
