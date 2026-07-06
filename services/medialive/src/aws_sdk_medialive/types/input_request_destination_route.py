"""Generated from Smithy shape ``com.amazonaws.medialive#InputRequestDestinationRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputRequestDestinationRoute(TypedDict, closed=True):
    cidr: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The CIDR of the route."""
    gateway: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An optional gateway for the route."""


# --- restJson1 ser/de ---
def serialize_json(value: InputRequestDestinationRoute) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "gateway" in value:
        out["gateway"] = value["gateway"]
    return out


def deserialize_json(data: dict) -> InputRequestDestinationRoute:
    out: InputRequestDestinationRoute = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    if "gateway" in data:
        out["gateway"] = data["gateway"]
    return out
