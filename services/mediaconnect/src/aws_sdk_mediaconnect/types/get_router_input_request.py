"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn


class GetRouterInputRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouterInputRequest:
    out: GetRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out
