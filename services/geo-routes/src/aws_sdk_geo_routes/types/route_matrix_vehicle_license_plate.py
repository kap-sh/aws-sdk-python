"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixVehicleLicensePlate``."""

from typing_extensions import NotRequired, TypedDict


class RouteMatrixVehicleLicensePlate(TypedDict, closed=True):
    last_character: NotRequired["str"]
    """<p>The last character of the License Plate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixVehicleLicensePlate) -> dict:
    out: dict = {}
    if "last_character" in value:
        out["LastCharacter"] = value["last_character"]
    return out


def deserialize_json(data: dict) -> RouteMatrixVehicleLicensePlate:
    out: RouteMatrixVehicleLicensePlate = {}  # type: ignore[typeddict-item]
    if "LastCharacter" in data:
        out["last_character"] = data["LastCharacter"]
    return out
