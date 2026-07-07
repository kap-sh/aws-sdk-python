"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeBridgeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_arn


class DescribeBridgeRequest(TypedDict, closed=True):
    bridge_arn: "aws_sdk_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBridgeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBridgeRequest:
    out: DescribeBridgeRequest = {}  # type: ignore[typeddict-item]
    return out
