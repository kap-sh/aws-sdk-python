"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeOutputsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_add_bridge_output_request
    import capo_mediaconnect.types.bridge_arn


class AddBridgeOutputsRequest(TypedDict, closed=True):
    bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    outputs: NotRequired[
        "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
    ]
    """<p> The outputs that you want to add to this bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeOutputsRequest) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_mediaconnect.types.__list_of_add_bridge_output_request

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_add_bridge_output_request.serialize_json(
                value["outputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddBridgeOutputsRequest:
    out: AddBridgeOutputsRequest = {}  # type: ignore[typeddict-item]
    if "outputs" in data:
        import capo_mediaconnect.types.__list_of_add_bridge_output_request

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_add_bridge_output_request.deserialize_json(
                data["outputs"]
            )
        )
    return out
