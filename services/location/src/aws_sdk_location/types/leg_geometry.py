"""Generated from Smithy shape ``com.amazonaws.location#LegGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.line_string


class LegGeometry(TypedDict, closed=True):
    line_string: NotRequired["aws_sdk_location.types.line_string.LineString"]
    """<p>An ordered list of positions used to plot a route on a map. </p> <p>The first position is closest to the start position for the leg, and the last position is the closest to the end position for the leg.</p> <ul> <li> <p>For example, <code>[[-123.117, 49.284],[-123.115, 49.285],[-123.115, 49.285]]</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LegGeometry) -> dict:
    out: dict = {}
    if "line_string" in value:
        import aws_sdk_location.types.line_string

        out["LineString"] = aws_sdk_location.types.line_string.serialize_json(
            value["line_string"]
        )
    return out


def deserialize_json(data: dict) -> LegGeometry:
    out: LegGeometry = {}  # type: ignore[typeddict-item]
    if "LineString" in data:
        import aws_sdk_location.types.line_string

        out["line_string"] = aws_sdk_location.types.line_string.deserialize_json(
            data["LineString"]
        )
    return out
