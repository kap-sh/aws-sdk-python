"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterInputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input


class UpdateRouterInputResponse(TypedDict):
    router_input: "aws_sdk_mediaconnect.types.router_input.RouterInput"
    """<p>The updated router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterInputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_input

    out["routerInput"] = aws_sdk_mediaconnect.types.router_input.serialize_json(
        value["router_input"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRouterInputResponse:
    out: UpdateRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "routerInput" in data:
        import aws_sdk_mediaconnect.types.router_input

        out["router_input"] = aws_sdk_mediaconnect.types.router_input.deserialize_json(
            data["routerInput"]
        )
    else:
        raise DeserializationError("UpdateRouterInputResponse.router_input required")
    return out
