"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn


class GetRouterInputRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouterInputRequest:
    out: GetRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out
