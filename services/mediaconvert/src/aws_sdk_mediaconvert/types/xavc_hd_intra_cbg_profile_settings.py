"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdIntraCbgProfileSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_class


class XavcHdIntraCbgProfileSettings(TypedDict, closed=True):
    xavc_class: NotRequired[
        "aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_class.XavcHdIntraCbgProfileClass"
    ]
    """Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""


# --- restJson1 ser/de ---
def serialize_json(value: XavcHdIntraCbgProfileSettings) -> dict:
    out: dict = {}
    if "xavc_class" in value:
        import aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_class

        out["xavcClass"] = (
            aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_class.serialize_json(
                value["xavc_class"]
            )
        )
    return out


def deserialize_json(data: dict) -> XavcHdIntraCbgProfileSettings:
    out: XavcHdIntraCbgProfileSettings = {}  # type: ignore[typeddict-item]
    if "xavcClass" in data:
        import aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_class

        out["xavc_class"] = (
            aws_sdk_mediaconvert.types.xavc_hd_intra_cbg_profile_class.deserialize_json(
                data["xavcClass"]
            )
        )
    return out
