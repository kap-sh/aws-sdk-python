"""Generated from Smithy shape ``com.amazonaws.s3outposts#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3outposts.types.network_interface_id


class NetworkInterface(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "capo_s3outposts.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID for the network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterface) -> dict:
    out: dict = {}
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_json(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    return out
