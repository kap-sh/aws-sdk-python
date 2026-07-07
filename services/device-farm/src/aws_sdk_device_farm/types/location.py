"""Generated from Smithy shape ``com.amazonaws.devicefarm#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.double


class Location(TypedDict, closed=True):
    latitude: "aws_sdk_device_farm.types.double.Double"
    """<p>The latitude.</p>"""
    longitude: "aws_sdk_device_farm.types.double.Double"
    """<p>The longitude.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Location) -> dict:
    out: dict = {}
    out["latitude"] = value["latitude"]
    out["longitude"] = value["longitude"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "latitude" in data:
        out["latitude"] = data["latitude"]
    else:
        raise DeserializationError("Location.latitude required")
    if "longitude" in data:
        out["longitude"] = data["longitude"]
    else:
        raise DeserializationError("Location.longitude required")
    return out
