"""Generated from Smithy shape ``com.amazonaws.medialive#InputDestinationRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class InputDestinationRoute(TypedDict, closed=True):
    cidr: NotRequired["capo_medialive.types.__string.__string"]
    """The CIDR of the route."""
    gateway: NotRequired["capo_medialive.types.__string.__string"]
    """An optional gateway for the route."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDestinationRoute) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "gateway" in value:
        out["gateway"] = value["gateway"]
    return out


def deserialize_json(data: dict) -> InputDestinationRoute:
    out: InputDestinationRoute = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    if "gateway" in data:
        out["gateway"] = data["gateway"]
    return out
