"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_flow_source
    import capo_mediaconnect.types.bridge_network_source


class BridgeSource(TypedDict, closed=True):
    flow_source: NotRequired[
        "capo_mediaconnect.types.bridge_flow_source.BridgeFlowSource"
    ]
    """<p> The source of the associated flow. </p>"""
    network_source: NotRequired[
        "capo_mediaconnect.types.bridge_network_source.BridgeNetworkSource"
    ]
    """<p> The network source for the bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BridgeSource) -> dict:
    out: dict = {}
    if "flow_source" in value:
        import capo_mediaconnect.types.bridge_flow_source

        out["flowSource"] = capo_mediaconnect.types.bridge_flow_source.serialize_json(
            value["flow_source"]
        )
    if "network_source" in value:
        import capo_mediaconnect.types.bridge_network_source

        out["networkSource"] = (
            capo_mediaconnect.types.bridge_network_source.serialize_json(
                value["network_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> BridgeSource:
    out: BridgeSource = {}  # type: ignore[typeddict-item]
    if "flowSource" in data:
        import capo_mediaconnect.types.bridge_flow_source

        out["flow_source"] = (
            capo_mediaconnect.types.bridge_flow_source.deserialize_json(
                data["flowSource"]
            )
        )
    if "networkSource" in data:
        import capo_mediaconnect.types.bridge_network_source

        out["network_source"] = (
            capo_mediaconnect.types.bridge_network_source.deserialize_json(
                data["networkSource"]
            )
        )
    return out
