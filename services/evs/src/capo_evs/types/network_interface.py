"""Generated from Smithy shape ``com.amazonaws.evs#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.network_interface_id


class NetworkInterface(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "capo_evs.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The unique ID of the elastic network interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterface) -> dict:
    out: dict = {}
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "networkInterfaceId" in data:
        out["network_interface_id"] = data["networkInterfaceId"]
    return out
