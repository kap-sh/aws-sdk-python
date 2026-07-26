"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output


class UpdateRouterOutputResponse(TypedDict, closed=True):
    router_output: "capo_mediaconnect.types.router_output.RouterOutput"
    """<p>The updated router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterOutputResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_output

    out["routerOutput"] = capo_mediaconnect.types.router_output.serialize_json(
        value["router_output"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRouterOutputResponse:
    out: UpdateRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "routerOutput" in data:
        import capo_mediaconnect.types.router_output

        out["router_output"] = capo_mediaconnect.types.router_output.deserialize_json(
            data["routerOutput"]
        )
    else:
        raise DeserializationError("UpdateRouterOutputResponse.router_output required")
    return out
