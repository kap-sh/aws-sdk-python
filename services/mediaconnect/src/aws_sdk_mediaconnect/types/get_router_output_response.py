"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterOutputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output


class GetRouterOutputResponse(TypedDict):
    router_output: "aws_sdk_mediaconnect.types.router_output.RouterOutput"
    """<p>The details of the requested router output, including its configuration, state, and other attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterOutputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_output

    out["routerOutput"] = aws_sdk_mediaconnect.types.router_output.serialize_json(
        value["router_output"]
    )
    return out


def deserialize_json(data: dict) -> GetRouterOutputResponse:
    out: GetRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "routerOutput" in data:
        import aws_sdk_mediaconnect.types.router_output

        out["router_output"] = (
            aws_sdk_mediaconnect.types.router_output.deserialize_json(
                data["routerOutput"]
            )
        )
    else:
        raise DeserializationError("GetRouterOutputResponse.router_output required")
    return out
