"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveBridgeOutputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_arn


class RemoveBridgeOutputRequest(TypedDict):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    output_name: "str"
    """<p> The name of the bridge output that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveBridgeOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveBridgeOutputRequest:
    out: RemoveBridgeOutputRequest = {}  # type: ignore[typeddict-item]
    return out
