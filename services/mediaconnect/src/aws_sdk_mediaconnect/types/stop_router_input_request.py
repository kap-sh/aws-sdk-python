"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StopRouterInputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn


class StopRouterInputRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopRouterInputRequest:
    out: StopRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out
