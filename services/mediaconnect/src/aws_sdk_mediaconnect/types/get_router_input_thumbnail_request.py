"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputThumbnailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn


class GetRouterInputThumbnailRequest(TypedDict, closed=True):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to see a thumbnail of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputThumbnailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouterInputThumbnailRequest:
    out: GetRouterInputThumbnailRequest = {}  # type: ignore[typeddict-item]
    return out
