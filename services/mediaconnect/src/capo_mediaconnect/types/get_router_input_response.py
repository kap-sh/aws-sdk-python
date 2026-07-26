"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input


class GetRouterInputResponse(TypedDict, closed=True):
    router_input: "capo_mediaconnect.types.router_input.RouterInput"
    """<p>The details of the requested router input, including its configuration, state, and other attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_input

    out["routerInput"] = capo_mediaconnect.types.router_input.serialize_json(
        value["router_input"]
    )
    return out


def deserialize_json(data: dict) -> GetRouterInputResponse:
    out: GetRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "routerInput" in data:
        import capo_mediaconnect.types.router_input

        out["router_input"] = capo_mediaconnect.types.router_input.deserialize_json(
            data["routerInput"]
        )
    else:
        raise DeserializationError("GetRouterInputResponse.router_input required")
    return out
