"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kIntraCbgProfileSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_class


class Xavc4kIntraCbgProfileSettings(TypedDict):
    xavc_class: NotRequired[
        "aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_class.Xavc4kIntraCbgProfileClass"
    ]
    """Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kIntraCbgProfileSettings) -> dict:
    out: dict = {}
    if "xavc_class" in value:
        import aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_class

        out["xavcClass"] = (
            aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_class.serialize_json(
                value["xavc_class"]
            )
        )
    return out


def deserialize_json(data: dict) -> Xavc4kIntraCbgProfileSettings:
    out: Xavc4kIntraCbgProfileSettings = {}  # type: ignore[typeddict-item]
    if "xavcClass" in data:
        import aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_class

        out["xavc_class"] = (
            aws_sdk_mediaconvert.types.xavc4k_intra_cbg_profile_class.deserialize_json(
                data["xavcClass"]
            )
        )
    return out
