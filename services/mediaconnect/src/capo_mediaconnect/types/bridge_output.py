"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_flow_output
    import capo_mediaconnect.types.bridge_network_output


class BridgeOutput(TypedDict, closed=True):
    flow_output: NotRequired[
        "capo_mediaconnect.types.bridge_flow_output.BridgeFlowOutput"
    ]
    """<p> The output of the associated flow. </p>"""
    network_output: NotRequired[
        "capo_mediaconnect.types.bridge_network_output.BridgeNetworkOutput"
    ]
    """<p> The network output for the bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BridgeOutput) -> dict:
    out: dict = {}
    if "flow_output" in value:
        import capo_mediaconnect.types.bridge_flow_output

        out["flowOutput"] = capo_mediaconnect.types.bridge_flow_output.serialize_json(
            value["flow_output"]
        )
    if "network_output" in value:
        import capo_mediaconnect.types.bridge_network_output

        out["networkOutput"] = (
            capo_mediaconnect.types.bridge_network_output.serialize_json(
                value["network_output"]
            )
        )
    return out


def deserialize_json(data: dict) -> BridgeOutput:
    out: BridgeOutput = {}  # type: ignore[typeddict-item]
    if "flowOutput" in data:
        import capo_mediaconnect.types.bridge_flow_output

        out["flow_output"] = (
            capo_mediaconnect.types.bridge_flow_output.deserialize_json(
                data["flowOutput"]
            )
        )
    if "networkOutput" in data:
        import capo_mediaconnect.types.bridge_network_output

        out["network_output"] = (
            capo_mediaconnect.types.bridge_network_output.deserialize_json(
                data["networkOutput"]
            )
        )
    return out
