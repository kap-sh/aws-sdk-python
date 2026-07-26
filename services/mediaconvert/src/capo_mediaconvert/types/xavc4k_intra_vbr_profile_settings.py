"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kIntraVbrProfileSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.xavc4k_intra_vbr_profile_class


class Xavc4kIntraVbrProfileSettings(TypedDict, closed=True):
    xavc_class: NotRequired[
        "capo_mediaconvert.types.xavc4k_intra_vbr_profile_class.Xavc4kIntraVbrProfileClass"
    ]
    """Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kIntraVbrProfileSettings) -> dict:
    out: dict = {}
    if "xavc_class" in value:
        import capo_mediaconvert.types.xavc4k_intra_vbr_profile_class

        out["xavcClass"] = (
            capo_mediaconvert.types.xavc4k_intra_vbr_profile_class.serialize_json(
                value["xavc_class"]
            )
        )
    return out


def deserialize_json(data: dict) -> Xavc4kIntraVbrProfileSettings:
    out: Xavc4kIntraVbrProfileSettings = {}  # type: ignore[typeddict-item]
    if "xavcClass" in data:
        import capo_mediaconvert.types.xavc4k_intra_vbr_profile_class

        out["xavc_class"] = (
            capo_mediaconvert.types.xavc4k_intra_vbr_profile_class.deserialize_json(
                data["xavcClass"]
            )
        )
    return out
