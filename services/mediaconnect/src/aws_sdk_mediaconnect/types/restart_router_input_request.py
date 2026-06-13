"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RestartRouterInputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn


class RestartRouterInputRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to restart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestartRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestartRouterInputRequest:
    out: RestartRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out
