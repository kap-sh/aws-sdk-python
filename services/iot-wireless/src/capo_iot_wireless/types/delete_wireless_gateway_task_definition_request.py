"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteWirelessGatewayTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_task_definition_id


class DeleteWirelessGatewayTaskDefinitionRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWirelessGatewayTaskDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWirelessGatewayTaskDefinitionRequest:
    out: DeleteWirelessGatewayTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
