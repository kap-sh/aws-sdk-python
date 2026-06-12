"""Generated from Smithy shape ``com.amazonaws.medialive#IpPoolUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class IpPoolUpdateRequest(TypedDict):
    cidr: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A CIDR block of IP addresses to reserve for MediaLive Anywhere."""


# --- restJson1 ser/de ---
def serialize_json(value: IpPoolUpdateRequest) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> IpPoolUpdateRequest:
    out: IpPoolUpdateRequest = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
