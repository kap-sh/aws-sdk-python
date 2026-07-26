"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StopRouterOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_state


class StopRouterOutputResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The ARN of the router output that was stopped.</p>"""
    name: "str"
    """<p>The name of the router output that was stopped.</p>"""
    state: "capo_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The current state of the router output after being stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRouterOutputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_output_state

    out["state"] = capo_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> StopRouterOutputResponse:
    out: StopRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StopRouterOutputResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StopRouterOutputResponse.name required")
    if "state" in data:
        import capo_mediaconnect.types.router_output_state

        out["state"] = capo_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("StopRouterOutputResponse.state required")
    return out
