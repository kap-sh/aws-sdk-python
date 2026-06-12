"""Generated from Smithy shape ``com.amazonaws.medialive#IpPool``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class IpPool(TypedDict):
    cidr: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A CIDR block of IP addresses that are reserved for MediaLive Anywhere."""


# --- restJson1 ser/de ---
def serialize_json(value: IpPool) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> IpPool:
    out: IpPool = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
