"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_arn


class DeleteRouterOutputRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouterOutputRequest:
    out: DeleteRouterOutputRequest = {}  # type: ignore[typeddict-item]
    return out
