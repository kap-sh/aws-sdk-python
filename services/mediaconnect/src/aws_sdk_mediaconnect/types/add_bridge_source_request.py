"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.add_bridge_flow_source_request
    import aws_sdk_mediaconnect.types.add_bridge_network_source_request

class AddBridgeSourceRequest(TypedDict):
    flow_source: NotRequired["aws_sdk_mediaconnect.types.add_bridge_flow_source_request.AddBridgeFlowSourceRequest"]
    """<p> The source of the flow. </p>"""
    network_source: NotRequired["aws_sdk_mediaconnect.types.add_bridge_network_source_request.AddBridgeNetworkSourceRequest"]
    """<p> The source of the network. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeSourceRequest) -> dict:
    out: dict = {}
    if "flow_source" in value:
        import aws_sdk_mediaconnect.types.add_bridge_flow_source_request
        out["flowSource"] = aws_sdk_mediaconnect.types.add_bridge_flow_source_request.serialize_json(value["flow_source"])
    if "network_source" in value:
        import aws_sdk_mediaconnect.types.add_bridge_network_source_request
        out["networkSource"] = aws_sdk_mediaconnect.types.add_bridge_network_source_request.serialize_json(value["network_source"])
    return out


def deserialize_json(data: dict) -> AddBridgeSourceRequest:
    out: AddBridgeSourceRequest = {}  # type: ignore[typeddict-item]
    if "flowSource" in data:
        import aws_sdk_mediaconnect.types.add_bridge_flow_source_request
        out["flow_source"] = aws_sdk_mediaconnect.types.add_bridge_flow_source_request.deserialize_json(data["flowSource"])
    if "networkSource" in data:
        import aws_sdk_mediaconnect.types.add_bridge_network_source_request
        out["network_source"] = aws_sdk_mediaconnect.types.add_bridge_network_source_request.deserialize_json(data["networkSource"])
    return out