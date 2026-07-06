"""Generated from Smithy shape ``com.amazonaws.location#TruckDimensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.dimension_unit
    import aws_sdk_location.types.sensitive_double


class TruckDimensions(TypedDict, closed=True):
    length: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The length of the truck.</p> <ul> <li> <p>For example, <code>15.5</code>.</p> </li> </ul> <note> <p> For routes calculated with a HERE resource, this value must be between 0 and 300 meters. </p> </note>"""
    height: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The height of the truck.</p> <ul> <li> <p>For example, <code>4.5</code>.</p> </li> </ul> <note> <p> For routes calculated with a HERE resource, this value must be between 0 and 50 meters. </p> </note>"""
    width: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The width of the truck.</p> <ul> <li> <p>For example, <code>4.5</code>.</p> </li> </ul> <note> <p> For routes calculated with a HERE resource, this value must be between 0 and 50 meters. </p> </note>"""
    unit: NotRequired["aws_sdk_location.types.dimension_unit.DimensionUnit"]
    """<p> Specifies the unit of measurement for the truck dimensions.</p> <p>Default Value: <code>Meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TruckDimensions) -> dict:
    out: dict = {}
    if "length" in value:
        out["Length"] = value["length"]
    if "height" in value:
        out["Height"] = value["height"]
    if "width" in value:
        out["Width"] = value["width"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> TruckDimensions:
    out: TruckDimensions = {}  # type: ignore[typeddict-item]
    if "Length" in data:
        out["length"] = data["Length"]
    if "Height" in data:
        out["height"] = data["Height"]
    if "Width" in data:
        out["width"] = data["Width"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
