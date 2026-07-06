"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RestartRouterOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_arn


class RestartRouterOutputRequest(TypedDict, closed=True):
    arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that you want to restart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestartRouterOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestartRouterOutputRequest:
    out: RestartRouterOutputRequest = {}  # type: ignore[typeddict-item]
    return out
