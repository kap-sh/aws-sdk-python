"""Generated from Smithy shape ``com.amazonaws.medialive#IpPoolCreateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class IpPoolCreateRequest(TypedDict, closed=True):
    cidr: NotRequired["capo_medialive.types.__string.__string"]
    """A CIDR block of IP addresses to reserve for MediaLive Anywhere."""


# --- restJson1 ser/de ---
def serialize_json(value: IpPoolCreateRequest) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> IpPoolCreateRequest:
    out: IpPoolCreateRequest = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
