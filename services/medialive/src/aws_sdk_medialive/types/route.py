"""Generated from Smithy shape ``com.amazonaws.medialive#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class Route(TypedDict, closed=True):
    cidr: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A CIDR block for one Route."""
    gateway: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The IP address of the Gateway for this route, if applicable."""


# --- restJson1 ser/de ---
def serialize_json(value: Route) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "gateway" in value:
        out["gateway"] = value["gateway"]
    return out


def deserialize_json(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    if "gateway" in data:
        out["gateway"] = data["gateway"]
    return out
