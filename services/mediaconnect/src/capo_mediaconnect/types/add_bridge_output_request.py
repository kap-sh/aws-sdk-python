"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.add_bridge_network_output_request


class AddBridgeOutputRequest(TypedDict, closed=True):
    network_output: NotRequired[
        "capo_mediaconnect.types.add_bridge_network_output_request.AddBridgeNetworkOutputRequest"
    ]
    """<p> The network output of the bridge. A network output is delivered to your premises. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeOutputRequest) -> dict:
    out: dict = {}
    if "network_output" in value:
        import capo_mediaconnect.types.add_bridge_network_output_request

        out["networkOutput"] = (
            capo_mediaconnect.types.add_bridge_network_output_request.serialize_json(
                value["network_output"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddBridgeOutputRequest:
    out: AddBridgeOutputRequest = {}  # type: ignore[typeddict-item]
    if "networkOutput" in data:
        import capo_mediaconnect.types.add_bridge_network_output_request

        out["network_output"] = (
            capo_mediaconnect.types.add_bridge_network_output_request.deserialize_json(
                data["networkOutput"]
            )
        )
    return out
