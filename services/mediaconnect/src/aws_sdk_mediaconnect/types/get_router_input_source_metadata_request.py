"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputSourceMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn


class GetRouterInputSourceMetadataRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input to retrieve metadata for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputSourceMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouterInputSourceMetadataRequest:
    out: GetRouterInputSourceMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
