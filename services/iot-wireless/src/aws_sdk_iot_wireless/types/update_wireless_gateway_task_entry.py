"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessGatewayTaskEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_entry
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_arn
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id


class UpdateWirelessGatewayTaskEntry(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    ]
    """<p>The ID of the new wireless gateway task entry.</p>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_entry.LoRaWANUpdateGatewayTaskEntry"
    ]
    """<p>The properties that relate to the LoRaWAN wireless gateway.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_arn.WirelessGatewayTaskDefinitionArn"
    ]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessGatewayTaskEntry) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_entry

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_entry.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UpdateWirelessGatewayTaskEntry:
    out: UpdateWirelessGatewayTaskEntry = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_entry

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_entry.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
