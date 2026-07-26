"""Generated from Smithy shape ``com.amazonaws.devicefarm#Resolution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.integer


class Resolution(TypedDict, closed=True):
    width: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The screen resolution's width, expressed in pixels.</p>"""
    height: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The screen resolution's height, expressed in pixels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resolution) -> dict:
    out: dict = {}
    if "width" in value:
        out["width"] = value["width"]
    if "height" in value:
        out["height"] = value["height"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resolution:
    out: Resolution = {}  # type: ignore[typeddict-item]
    if "width" in data:
        out["width"] = data["width"]
    if "height" in data:
        out["height"] = data["height"]
    return out
