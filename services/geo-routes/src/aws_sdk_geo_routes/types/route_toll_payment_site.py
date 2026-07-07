"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentSite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position23


class RouteTollPaymentSite(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>Name of the payment site.</p>"""
    position: "aws_sdk_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPaymentSite) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_geo_routes.types.position23

    out["Position"] = aws_sdk_geo_routes.types.position23.serialize_json(
        value["position"]
    )
    return out


def deserialize_json(data: dict) -> RouteTollPaymentSite:
    out: RouteTollPaymentSite = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Position" in data:
        import aws_sdk_geo_routes.types.position23

        out["position"] = aws_sdk_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteTollPaymentSite.position required")
    return out
