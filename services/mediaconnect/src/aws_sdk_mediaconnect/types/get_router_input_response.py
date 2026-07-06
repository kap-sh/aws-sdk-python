"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input


class GetRouterInputResponse(TypedDict, closed=True):
    router_input: "aws_sdk_mediaconnect.types.router_input.RouterInput"
    """<p>The details of the requested router input, including its configuration, state, and other attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_input

    out["routerInput"] = aws_sdk_mediaconnect.types.router_input.serialize_json(
        value["router_input"]
    )
    return out


def deserialize_json(data: dict) -> GetRouterInputResponse:
    out: GetRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "routerInput" in data:
        import aws_sdk_mediaconnect.types.router_input

        out["router_input"] = aws_sdk_mediaconnect.types.router_input.deserialize_json(
            data["routerInput"]
        )
    else:
        raise DeserializationError("GetRouterInputResponse.router_input required")
    return out
