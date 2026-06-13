"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterOutputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_arn


class GetRouterOutputRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that you want to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouterOutputRequest:
    out: GetRouterOutputRequest = {}  # type: ignore[typeddict-item]
    return out
