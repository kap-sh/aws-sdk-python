"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterResizeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterResizeInfo(TypedDict, closed=True):
    allow_cancel_resize: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the resize operation can be canceled.</p>"""
    resize_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resize operation.</p> <p>Valid values: <code>ClassicResize</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterResizeInfo) -> dict:
    out: dict = {}
    if "allow_cancel_resize" in value:
        out["AllowCancelResize"] = value["allow_cancel_resize"]
    if "resize_type" in value:
        out["ResizeType"] = value["resize_type"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterResizeInfo:
    out: AwsRedshiftClusterResizeInfo = {}  # type: ignore[typeddict-item]
    if "AllowCancelResize" in data:
        out["allow_cancel_resize"] = data["AllowCancelResize"]
    if "ResizeType" in data:
        out["resize_type"] = data["ResizeType"]
    return out
