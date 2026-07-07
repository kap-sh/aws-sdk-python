"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.destination_name


class DeleteDestinationRequest(TypedDict, closed=True):
    name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName"
    """<p>The id of the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDestinationRequest:
    out: DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
