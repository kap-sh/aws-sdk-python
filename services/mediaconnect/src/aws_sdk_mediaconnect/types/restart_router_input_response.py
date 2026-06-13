"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RestartRouterInputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_input_state


class RestartRouterInputResponse(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The ARN of the router input that was restarted.</p>"""
    name: "str"
    """<p>The name of the router input that was restarted.</p>"""
    state: "aws_sdk_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The current state of the router input after the restart operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestartRouterInputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_input_state

    out["state"] = aws_sdk_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> RestartRouterInputResponse:
    out: RestartRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RestartRouterInputResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RestartRouterInputResponse.name required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_input_state

        out["state"] = aws_sdk_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("RestartRouterInputResponse.state required")
    return out
