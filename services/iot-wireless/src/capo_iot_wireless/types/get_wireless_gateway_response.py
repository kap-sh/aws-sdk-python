"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.lo_ra_wan_gateway
    import capo_iot_wireless.types.thing_arn
    import capo_iot_wireless.types.thing_name
    import capo_iot_wireless.types.wireless_gateway_arn
    import capo_iot_wireless.types.wireless_gateway_id
    import capo_iot_wireless.types.wireless_gateway_name


class GetWirelessGatewayResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
    ]
    """<p>The name of the resource.</p>"""
    id: NotRequired["capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"]
    """<p>The ID of the wireless gateway.</p>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    lo_ra_wan: NotRequired["capo_iot_wireless.types.lo_ra_wan_gateway.LoRaWANGateway"]
    """<p>Information about the wireless gateway.</p>"""
    arn: NotRequired["capo_iot_wireless.types.wireless_gateway_arn.WirelessGatewayArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    thing_name: NotRequired["capo_iot_wireless.types.thing_name.ThingName"]
    """<p>The name of the thing associated with the wireless gateway. The value is empty if a thing isn't associated with the gateway.</p>"""
    thing_arn: NotRequired["capo_iot_wireless.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing associated with the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_gateway

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_gateway.serialize_json(
            value["lo_ra_wan"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "thing_name" in value:
        out["ThingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["ThingArn"] = value["thing_arn"]
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayResponse:
    out: GetWirelessGatewayResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_gateway

        out["lo_ra_wan"] = capo_iot_wireless.types.lo_ra_wan_gateway.deserialize_json(
            data["LoRaWAN"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ThingName" in data:
        out["thing_name"] = data["ThingName"]
    if "ThingArn" in data:
        out["thing_arn"] = data["ThingArn"]
    return out
