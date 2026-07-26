"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_arn_list


class BatchGetRouterOutputRequest(TypedDict, closed=True):
    arns: "capo_mediaconnect.types.router_output_arn_list.RouterOutputArnList"
    """<p>The Amazon Resource Names (ARNs) of the router outputs you want to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetRouterOutputRequest:
    out: BatchGetRouterOutputRequest = {}  # type: ignore[typeddict-item]
    return out
