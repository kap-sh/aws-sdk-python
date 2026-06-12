"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.destination_name


class GetDestinationRequest(TypedDict):
    name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName"
    """<p>The name of the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDestinationRequest:
    out: GetDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
