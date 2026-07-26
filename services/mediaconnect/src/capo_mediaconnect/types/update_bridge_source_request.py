"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_arn
    import capo_mediaconnect.types.update_bridge_flow_source_request
    import capo_mediaconnect.types.update_bridge_network_source_request


class UpdateBridgeSourceRequest(TypedDict, closed=True):
    bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    flow_source: NotRequired[
        "capo_mediaconnect.types.update_bridge_flow_source_request.UpdateBridgeFlowSourceRequest"
    ]
    """<p> The name of the flow that you want to update.</p>"""
    network_source: NotRequired[
        "capo_mediaconnect.types.update_bridge_network_source_request.UpdateBridgeNetworkSourceRequest"
    ]
    """<p> The network for the bridge source. </p>"""
    source_name: "str"
    """<p> The name of the source that you want to update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeSourceRequest) -> dict:
    out: dict = {}
    if "flow_source" in value:
        import capo_mediaconnect.types.update_bridge_flow_source_request

        out["flowSource"] = (
            capo_mediaconnect.types.update_bridge_flow_source_request.serialize_json(
                value["flow_source"]
            )
        )
    if "network_source" in value:
        import capo_mediaconnect.types.update_bridge_network_source_request

        out["networkSource"] = (
            capo_mediaconnect.types.update_bridge_network_source_request.serialize_json(
                value["network_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeSourceRequest:
    out: UpdateBridgeSourceRequest = {}  # type: ignore[typeddict-item]
    if "flowSource" in data:
        import capo_mediaconnect.types.update_bridge_flow_source_request

        out["flow_source"] = (
            capo_mediaconnect.types.update_bridge_flow_source_request.deserialize_json(
                data["flowSource"]
            )
        )
    if "networkSource" in data:
        import capo_mediaconnect.types.update_bridge_network_source_request

        out["network_source"] = (
            capo_mediaconnect.types.update_bridge_network_source_request.deserialize_json(
                data["networkSource"]
            )
        )
    return out
