"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeOutputRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_arn
    import aws_sdk_mediaconnect.types.update_bridge_network_output_request


class UpdateBridgeOutputRequest(TypedDict):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    network_output: NotRequired[
        "aws_sdk_mediaconnect.types.update_bridge_network_output_request.UpdateBridgeNetworkOutputRequest"
    ]
    """<p> The network of the bridge output. </p>"""
    output_name: "str"
    """<p> Tname of the output that you want to update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeOutputRequest) -> dict:
    out: dict = {}
    if "network_output" in value:
        import aws_sdk_mediaconnect.types.update_bridge_network_output_request

        out["networkOutput"] = (
            aws_sdk_mediaconnect.types.update_bridge_network_output_request.serialize_json(
                value["network_output"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeOutputRequest:
    out: UpdateBridgeOutputRequest = {}  # type: ignore[typeddict-item]
    if "networkOutput" in data:
        import aws_sdk_mediaconnect.types.update_bridge_network_output_request

        out["network_output"] = (
            aws_sdk_mediaconnect.types.update_bridge_network_output_request.deserialize_json(
                data["networkOutput"]
            )
        )
    return out
