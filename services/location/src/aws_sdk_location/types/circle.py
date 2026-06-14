"""Generated from Smithy shape ``com.amazonaws.location#Circle``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.position
    import aws_sdk_location.types.sensitive_double


class Circle(TypedDict):
    center: "aws_sdk_location.types.position.Position"
    r"""<p>A single point geometry, specifying the center of the circle, using <a href=\"https://gisgeography.com/wgs84-world-geodetic-system/\">WGS 84</a> coordinates, in the form <code>[longitude, latitude]</code>.</p>"""
    radius: "aws_sdk_location.types.sensitive_double.SensitiveDouble"
    """<p>The radius of the circle in meters. Must be greater than zero and no larger than 100,000 (100 kilometers).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Circle) -> dict:
    out: dict = {}
    import aws_sdk_location.types.position

    out["Center"] = aws_sdk_location.types.position.serialize_json(value["center"])
    out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> Circle:
    out: Circle = {}  # type: ignore[typeddict-item]
    if "Center" in data:
        import aws_sdk_location.types.position

        out["center"] = aws_sdk_location.types.position.deserialize_json(data["Center"])
    else:
        raise DeserializationError("Circle.center required")
    if "Radius" in data:
        out["radius"] = data["Radius"]
    else:
        raise DeserializationError("Circle.radius required")
    return out
