"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveBridgeSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_arn


class RemoveBridgeSourceRequest(TypedDict, closed=True):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    source_name: "str"
    """<p> The name of the bridge source that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveBridgeSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveBridgeSourceRequest:
    out: RemoveBridgeSourceRequest = {}  # type: ignore[typeddict-item]
    return out
