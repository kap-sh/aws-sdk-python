"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineVehicleLicensePlate``."""

from typing_extensions import NotRequired, TypedDict


class IsolineVehicleLicensePlate(TypedDict, closed=True):
    last_character: NotRequired["str"]
    """<p>The last character of the vehicle's license plate. Used to determine road access restrictions in regions with license plate-based traffic management systems.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineVehicleLicensePlate) -> dict:
    out: dict = {}
    if "last_character" in value:
        out["LastCharacter"] = value["last_character"]
    return out


def deserialize_json(data: dict) -> IsolineVehicleLicensePlate:
    out: IsolineVehicleLicensePlate = {}  # type: ignore[typeddict-item]
    if "LastCharacter" in data:
        out["last_character"] = data["LastCharacter"]
    return out
