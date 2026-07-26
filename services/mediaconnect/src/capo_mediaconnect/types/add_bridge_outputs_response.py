"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeOutputsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_bridge_output


class AddBridgeOutputsResponse(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge that you added outputs to.</p>"""
    outputs: NotRequired[
        "capo_mediaconnect.types.__list_of_bridge_output.__listOfBridgeOutput"
    ]
    """<p> The outputs that you added to this bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeOutputsResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "outputs" in value:
        import capo_mediaconnect.types.__list_of_bridge_output

        out["outputs"] = capo_mediaconnect.types.__list_of_bridge_output.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> AddBridgeOutputsResponse:
    out: AddBridgeOutputsResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "outputs" in data:
        import capo_mediaconnect.types.__list_of_bridge_output

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_bridge_output.deserialize_json(
                data["outputs"]
            )
        )
    return out
