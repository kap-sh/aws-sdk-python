"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.gateway


class CreateGatewayResponse(TypedDict, closed=True):
    gateway: NotRequired["capo_mediaconnect.types.gateway.Gateway"]
    """<p> The gateway that you created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayResponse) -> dict:
    out: dict = {}
    if "gateway" in value:
        import capo_mediaconnect.types.gateway

        out["gateway"] = capo_mediaconnect.types.gateway.serialize_json(
            value["gateway"]
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayResponse:
    out: CreateGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gateway" in data:
        import capo_mediaconnect.types.gateway

        out["gateway"] = capo_mediaconnect.types.gateway.deserialize_json(
            data["gateway"]
        )
    return out
