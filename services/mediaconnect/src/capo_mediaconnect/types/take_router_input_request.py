"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TakeRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_output_arn


class TakeRouterInputRequest(TypedDict, closed=True):
    router_output_arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that you want to associate with a router input.</p>"""
    router_input_arn: NotRequired[
        "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the router input that you want to associate with a router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TakeRouterInputRequest) -> dict:
    out: dict = {}
    if "router_input_arn" in value:
        out["routerInputArn"] = value["router_input_arn"]
    return out


def deserialize_json(data: dict) -> TakeRouterInputRequest:
    out: TakeRouterInputRequest = {}  # type: ignore[typeddict-item]
    if "routerInputArn" in data:
        out["router_input_arn"] = data["routerInputArn"]
    return out
