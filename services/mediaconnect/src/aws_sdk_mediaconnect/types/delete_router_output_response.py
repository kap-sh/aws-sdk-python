"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterOutputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_arn
    import aws_sdk_mediaconnect.types.router_output_state


class DeleteRouterOutputResponse(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The ARN of the deleted router output.</p>"""
    name: "str"
    """<p>The name of the deleted router output.</p>"""
    state: "aws_sdk_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The current state of the deleted router output, indicating where it is in the deletion process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterOutputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_output_state

    out["state"] = aws_sdk_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> DeleteRouterOutputResponse:
    out: DeleteRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteRouterOutputResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteRouterOutputResponse.name required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_output_state

        out["state"] = aws_sdk_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("DeleteRouterOutputResponse.state required")
    return out
