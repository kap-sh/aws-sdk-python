"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.endpoint


class GetEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired["capo_iotdeviceadvisor.types.endpoint.Endpoint"]
    """<p>The response of an Device Advisor endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> GetEndpointResponse:
    out: GetEndpointResponse = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    return out
