"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn_list


class BatchGetRouterInputRequest(TypedDict, closed=True):
    arns: "capo_mediaconnect.types.router_input_arn_list.RouterInputArnList"
    """<p>The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetRouterInputRequest:
    out: BatchGetRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out
