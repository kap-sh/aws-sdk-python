"""Generated from Smithy shape ``com.amazonaws.m2#GdgDetailAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.integer
    import aws_sdk_m2.types.string50


class GdgDetailAttributes(TypedDict, closed=True):
    limit: "aws_sdk_m2.types.integer.Integer"
    """<p>The maximum number of generation data sets, up to 255, in a GDG.</p>"""
    roll_disposition: NotRequired["aws_sdk_m2.types.string50.String50"]
    """<p>The disposition of the data set in the catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GdgDetailAttributes) -> dict:
    out: dict = {}
    out["limit"] = value.get("limit", 0)
    if "roll_disposition" in value:
        out["rollDisposition"] = value["roll_disposition"]
    return out


def deserialize_json(data: dict) -> GdgDetailAttributes:
    out: GdgDetailAttributes = {}  # type: ignore[typeddict-item]
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if "rollDisposition" in data:
        out["roll_disposition"] = data["rollDisposition"]
    return out
