"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetNetworkAnalyzerConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_arn
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_name
    import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list
    import aws_sdk_iot_wireless.types.trace_content
    import aws_sdk_iot_wireless.types.wireless_device_list
    import aws_sdk_iot_wireless.types.wireless_gateway_list


class GetNetworkAnalyzerConfigurationResponse(TypedDict, closed=True):
    trace_content: NotRequired["aws_sdk_iot_wireless.types.trace_content.TraceContent"]
    wireless_devices: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_list.WirelessDeviceList"
    ]
    """<p>List of wireless device resources that have been added to the network analyzer configuration.</p>"""
    wireless_gateways: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
    ]
    """<p>List of wireless gateway resources that have been added to the network analyzer configuration.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_configuration_arn.NetworkAnalyzerConfigurationArn"
    ]
    """<p>The Amazon Resource Name of the new resource.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"
    ]
    multicast_groups: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
    ]
    """<p>List of multicast group resources that have been added to the network analyzer configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkAnalyzerConfigurationResponse) -> dict:
    out: dict = {}
    if "trace_content" in value:
        import aws_sdk_iot_wireless.types.trace_content

        out["TraceContent"] = aws_sdk_iot_wireless.types.trace_content.serialize_json(
            value["trace_content"]
        )
    if "wireless_devices" in value:
        import aws_sdk_iot_wireless.types.wireless_device_list

        out["WirelessDevices"] = (
            aws_sdk_iot_wireless.types.wireless_device_list.serialize_json(
                value["wireless_devices"]
            )
        )
    if "wireless_gateways" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_list

        out["WirelessGateways"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_list.serialize_json(
                value["wireless_gateways"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "multicast_groups" in value:
        import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list

        out["MulticastGroups"] = (
            aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.serialize_json(
                value["multicast_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetNetworkAnalyzerConfigurationResponse:
    out: GetNetworkAnalyzerConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TraceContent" in data:
        import aws_sdk_iot_wireless.types.trace_content

        out["trace_content"] = (
            aws_sdk_iot_wireless.types.trace_content.deserialize_json(
                data["TraceContent"]
            )
        )
    if "WirelessDevices" in data:
        import aws_sdk_iot_wireless.types.wireless_device_list

        out["wireless_devices"] = (
            aws_sdk_iot_wireless.types.wireless_device_list.deserialize_json(
                data["WirelessDevices"]
            )
        )
    if "WirelessGateways" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_list

        out["wireless_gateways"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_list.deserialize_json(
                data["WirelessGateways"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "MulticastGroups" in data:
        import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list

        out["multicast_groups"] = (
            aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.deserialize_json(
                data["MulticastGroups"]
            )
        )
    return out
