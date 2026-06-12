"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterInputResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_mediaconnect.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_input_state

class DeleteRouterInputResponse(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The ARN of the deleted router input.</p>"""
    name: "str"
    """<p>The name of the deleted router input.</p>"""
    state: "aws_sdk_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The current state of the deleted router input, indicating where it is in the deletion process.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterInputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_input_state
    out["state"] = aws_sdk_mediaconnect.types.router_input_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> DeleteRouterInputResponse:
    out: DeleteRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteRouterInputResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteRouterInputResponse.name required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_input_state
        out["state"] = aws_sdk_mediaconnect.types.router_input_state.deserialize_json(data["state"])
    else:
        raise DeserializationError("DeleteRouterInputResponse.state required")
    return out