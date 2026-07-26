"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_task_definition_id


class GetWirelessGatewayTaskDefinitionRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    """<p>The ID of the resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayTaskDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayTaskDefinitionRequest:
    out: GetWirelessGatewayTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
