"""Generated from Smithy shape ``com.amazonaws.georoutes#Circle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.sensitive_double


class Circle(TypedDict, closed=True):
    center: "aws_sdk_geo_routes.types.position.Position"
    """<p>Center of the Circle in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <p>Example: <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>. </p>"""
    radius: "aws_sdk_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Radius of the Circle.</p> <p> <b>Unit</b>: <code>meters</code> </p> <p>Valid Range: Minimum value of 0. Maximum value of 200000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Circle) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.position

    out["Center"] = aws_sdk_geo_routes.types.position.serialize_json(value["center"])
    out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> Circle:
    out: Circle = {}  # type: ignore[typeddict-item]
    if "Center" in data:
        import aws_sdk_geo_routes.types.position

        out["center"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Center"]
        )
    else:
        raise DeserializationError("Circle.center required")
    if "Radius" in data:
        out["radius"] = data["Radius"]
    else:
        raise DeserializationError("Circle.radius required")
    return out
