"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.destination_name


class CreateDestinationResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_iot_managed_integrations.types.destination_name.DestinationName"
    ]
    """<p>The name of the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDestinationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDestinationResponse:
    out: CreateDestinationResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
