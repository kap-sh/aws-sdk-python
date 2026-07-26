"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StartRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn


class StartRouterInputRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartRouterInputRequest:
    out: StartRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out
