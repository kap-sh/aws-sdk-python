"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StopRouterOutputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_arn


class StopRouterOutputRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRouterOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopRouterOutputRequest:
    out: StopRouterOutputRequest = {}  # type: ignore[typeddict-item]
    return out
