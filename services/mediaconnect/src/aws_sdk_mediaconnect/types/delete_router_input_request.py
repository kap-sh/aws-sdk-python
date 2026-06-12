"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterInputRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn

class DeleteRouterInputRequest(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouterInputRequest:
    out: DeleteRouterInputRequest = {}  # type: ignore[typeddict-item]
    return out