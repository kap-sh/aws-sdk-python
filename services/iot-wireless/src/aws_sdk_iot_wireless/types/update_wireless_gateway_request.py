"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.gateway_max_eirp
    import aws_sdk_iot_wireless.types.join_eui_filters
    import aws_sdk_iot_wireless.types.net_id_filters
    import aws_sdk_iot_wireless.types.wireless_gateway_id
    import aws_sdk_iot_wireless.types.wireless_gateway_name


class UpdateWirelessGatewayRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
    ]
    """<p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>A new description of the resource.</p>"""
    join_eui_filters: NotRequired[
        "aws_sdk_iot_wireless.types.join_eui_filters.JoinEuiFilters"
    ]
    net_id_filters: NotRequired[
        "aws_sdk_iot_wireless.types.net_id_filters.NetIdFilters"
    ]
    max_eirp: NotRequired["aws_sdk_iot_wireless.types.gateway_max_eirp.GatewayMaxEirp"]
    """<p>The MaxEIRP value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessGatewayRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "join_eui_filters" in value:
        import aws_sdk_iot_wireless.types.join_eui_filters

        out["JoinEuiFilters"] = (
            aws_sdk_iot_wireless.types.join_eui_filters.serialize_json(
                value["join_eui_filters"]
            )
        )
    if "net_id_filters" in value:
        import aws_sdk_iot_wireless.types.net_id_filters

        out["NetIdFilters"] = aws_sdk_iot_wireless.types.net_id_filters.serialize_json(
            value["net_id_filters"]
        )
    if "max_eirp" in value:
        out["MaxEirp"] = value["max_eirp"]
    return out


def deserialize_json(data: dict) -> UpdateWirelessGatewayRequest:
    out: UpdateWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "JoinEuiFilters" in data:
        import aws_sdk_iot_wireless.types.join_eui_filters

        out["join_eui_filters"] = (
            aws_sdk_iot_wireless.types.join_eui_filters.deserialize_json(
                data["JoinEuiFilters"]
            )
        )
    if "NetIdFilters" in data:
        import aws_sdk_iot_wireless.types.net_id_filters

        out["net_id_filters"] = (
            aws_sdk_iot_wireless.types.net_id_filters.deserialize_json(
                data["NetIdFilters"]
            )
        )
    if "MaxEirp" in data:
        out["max_eirp"] = data["MaxEirp"]
    return out
