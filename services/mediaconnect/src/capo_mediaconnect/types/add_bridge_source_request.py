"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.add_bridge_flow_source_request
    import capo_mediaconnect.types.add_bridge_network_source_request


class AddBridgeSourceRequest(TypedDict, closed=True):
    flow_source: NotRequired[
        "capo_mediaconnect.types.add_bridge_flow_source_request.AddBridgeFlowSourceRequest"
    ]
    """<p> The source of the flow. </p>"""
    network_source: NotRequired[
        "capo_mediaconnect.types.add_bridge_network_source_request.AddBridgeNetworkSourceRequest"
    ]
    """<p> The source of the network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeSourceRequest) -> dict:
    out: dict = {}
    if "flow_source" in value:
        import capo_mediaconnect.types.add_bridge_flow_source_request

        out["flowSource"] = (
            capo_mediaconnect.types.add_bridge_flow_source_request.serialize_json(
                value["flow_source"]
            )
        )
    if "network_source" in value:
        import capo_mediaconnect.types.add_bridge_network_source_request

        out["networkSource"] = (
            capo_mediaconnect.types.add_bridge_network_source_request.serialize_json(
                value["network_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddBridgeSourceRequest:
    out: AddBridgeSourceRequest = {}  # type: ignore[typeddict-item]
    if "flowSource" in data:
        import capo_mediaconnect.types.add_bridge_flow_source_request

        out["flow_source"] = (
            capo_mediaconnect.types.add_bridge_flow_source_request.deserialize_json(
                data["flowSource"]
            )
        )
    if "networkSource" in data:
        import capo_mediaconnect.types.add_bridge_network_source_request

        out["network_source"] = (
            capo_mediaconnect.types.add_bridge_network_source_request.deserialize_json(
                data["networkSource"]
            )
        )
    return out
