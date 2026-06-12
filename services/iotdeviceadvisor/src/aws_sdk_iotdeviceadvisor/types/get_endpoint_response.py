"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.endpoint


class GetEndpointResponse(TypedDict):
    endpoint: NotRequired["aws_sdk_iotdeviceadvisor.types.endpoint.Endpoint"]
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
