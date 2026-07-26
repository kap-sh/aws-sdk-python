"""Generated from Smithy shape ``com.amazonaws.medialive#RouterDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class RouterDestinationSettings(TypedDict, closed=True):
    availability_zone_name: NotRequired["capo_medialive.types.__string.__string"]
    """Availability Zone for this MediaConnect Router destination."""


# --- restJson1 ser/de ---
def serialize_json(value: RouterDestinationSettings) -> dict:
    out: dict = {}
    if "availability_zone_name" in value:
        out["availabilityZoneName"] = value["availability_zone_name"]
    return out


def deserialize_json(data: dict) -> RouterDestinationSettings:
    out: RouterDestinationSettings = {}  # type: ignore[typeddict-item]
    if "availabilityZoneName" in data:
        out["availability_zone_name"] = data["availabilityZoneName"]
    return out
