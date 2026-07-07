"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleLicensePlate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_string


class RouteVehicleLicensePlate(TypedDict, closed=True):
    last_character: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>The last character of the License Plate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleLicensePlate) -> dict:
    out: dict = {}
    if "last_character" in value:
        out["LastCharacter"] = value["last_character"]
    return out


def deserialize_json(data: dict) -> RouteVehicleLicensePlate:
    out: RouteVehicleLicensePlate = {}  # type: ignore[typeddict-item]
    if "LastCharacter" in data:
        out["last_character"] = data["LastCharacter"]
    return out
