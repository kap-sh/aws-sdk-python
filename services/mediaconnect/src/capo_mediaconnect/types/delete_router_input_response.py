"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_state


class DeleteRouterInputResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The ARN of the deleted router input.</p>"""
    name: "str"
    """<p>The name of the deleted router input.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The current state of the deleted router input, indicating where it is in the deletion process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterInputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
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
        import capo_mediaconnect.types.router_input_state

        out["state"] = capo_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("DeleteRouterInputResponse.state required")
    return out
