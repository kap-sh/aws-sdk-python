"""Generated from Smithy shape ``com.amazonaws.vpclattice#IpResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.ip_address


class IpResource(TypedDict, closed=True):
    ip_address: NotRequired["aws_sdk_vpc_lattice.types.ip_address.IpAddress"]
    """<p>The IP address of the IP resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpResource) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> IpResource:
    out: IpResource = {}  # type: ignore[typeddict-item]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    return out
