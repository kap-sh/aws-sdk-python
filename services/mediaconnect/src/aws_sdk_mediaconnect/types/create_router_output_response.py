"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateRouterOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output


class CreateRouterOutputResponse(TypedDict, closed=True):
    router_output: "aws_sdk_mediaconnect.types.router_output.RouterOutput"
    """<p>The newly-created router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouterOutputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_output

    out["routerOutput"] = aws_sdk_mediaconnect.types.router_output.serialize_json(
        value["router_output"]
    )
    return out


def deserialize_json(data: dict) -> CreateRouterOutputResponse:
    out: CreateRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "routerOutput" in data:
        import aws_sdk_mediaconnect.types.router_output

        out["router_output"] = (
            aws_sdk_mediaconnect.types.router_output.deserialize_json(
                data["routerOutput"]
            )
        )
    else:
        raise DeserializationError("CreateRouterOutputResponse.router_output required")
    return out
