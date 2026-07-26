"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessGatewayWithThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.thing_arn
    import capo_iot_wireless.types.wireless_gateway_id


class AssociateWirelessGatewayWithThingRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""
    thing_arn: "capo_iot_wireless.types.thing_arn.ThingArn"
    """<p>The ARN of the thing to associate with the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessGatewayWithThingRequest) -> dict:
    out: dict = {}
    out["ThingArn"] = value["thing_arn"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessGatewayWithThingRequest:
    out: AssociateWirelessGatewayWithThingRequest = {}  # type: ignore[typeddict-item]
    if "ThingArn" in data:
        out["thing_arn"] = data["ThingArn"]
    else:
        raise DeserializationError(
            "AssociateWirelessGatewayWithThingRequest.thing_arn required"
        )
    return out
