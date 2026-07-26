"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input


class UpdateRouterInputResponse(TypedDict, closed=True):
    router_input: "capo_mediaconnect.types.router_input.RouterInput"
    """<p>The updated router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterInputResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_input

    out["routerInput"] = capo_mediaconnect.types.router_input.serialize_json(
        value["router_input"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRouterInputResponse:
    out: UpdateRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "routerInput" in data:
        import capo_mediaconnect.types.router_input

        out["router_input"] = capo_mediaconnect.types.router_input.deserialize_json(
            data["routerInput"]
        )
    else:
        raise DeserializationError("UpdateRouterInputResponse.router_input required")
    return out
