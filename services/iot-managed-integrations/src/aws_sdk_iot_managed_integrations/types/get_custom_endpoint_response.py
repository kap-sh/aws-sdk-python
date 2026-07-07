"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCustomEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.endpoint_address


class GetCustomEndpointResponse(TypedDict, closed=True):
    endpoint_address: (
        "aws_sdk_iot_managed_integrations.types.endpoint_address.EndpointAddress"
    )
    """<p>The IoT managed integrations dedicated, custom endpoint for the device to route traffic through.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomEndpointResponse) -> dict:
    out: dict = {}
    out["EndpointAddress"] = value["endpoint_address"]
    return out


def deserialize_json(data: dict) -> GetCustomEndpointResponse:
    out: GetCustomEndpointResponse = {}  # type: ignore[typeddict-item]
    if "EndpointAddress" in data:
        out["endpoint_address"] = data["EndpointAddress"]
    else:
        raise DeserializationError(
            "GetCustomEndpointResponse.endpoint_address required"
        )
    return out
