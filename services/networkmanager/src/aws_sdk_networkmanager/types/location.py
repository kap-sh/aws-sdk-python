"""Generated from Smithy shape ``com.amazonaws.networkmanager#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string


class Location(TypedDict, closed=True):
    address: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The physical address.</p>"""
    latitude: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The latitude.</p>"""
    longitude: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The longitude.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Location) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "latitude" in value:
        out["Latitude"] = value["latitude"]
    if "longitude" in value:
        out["Longitude"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Latitude" in data:
        out["latitude"] = data["Latitude"]
    if "Longitude" in data:
        out["longitude"] = data["Longitude"]
    return out
