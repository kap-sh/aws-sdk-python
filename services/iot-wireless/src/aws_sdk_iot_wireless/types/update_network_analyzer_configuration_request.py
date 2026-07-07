"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateNetworkAnalyzerConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_name
    import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list
    import aws_sdk_iot_wireless.types.trace_content
    import aws_sdk_iot_wireless.types.wireless_device_list
    import aws_sdk_iot_wireless.types.wireless_gateway_list


class UpdateNetworkAnalyzerConfigurationRequest(TypedDict, closed=True):
    configuration_name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"
    trace_content: NotRequired["aws_sdk_iot_wireless.types.trace_content.TraceContent"]
    wireless_devices_to_add: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_list.WirelessDeviceList"
    ]
    """<p>Wireless device resources to add to the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resource to add in the input array.</p>"""
    wireless_devices_to_remove: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_list.WirelessDeviceList"
    ]
    """<p>Wireless device resources to remove from the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resources to remove in the input array.</p>"""
    wireless_gateways_to_add: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
    ]
    """<p>Wireless gateway resources to add to the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resource to add in the input array.</p>"""
    wireless_gateways_to_remove: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
    ]
    """<p>Wireless gateway resources to remove from the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resources to remove in the input array.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    multicast_groups_to_add: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
    ]
    """<p>Multicast group resources to add to the network analyzer configuration. Provide the <code>MulticastGroupId</code> of the resource to add in the input array.</p>"""
    multicast_groups_to_remove: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
    ]
    """<p>Multicast group resources to remove from the network analyzer configuration. Provide the <code>MulticastGroupId</code> of the resources to remove in the input array.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkAnalyzerConfigurationRequest) -> dict:
    out: dict = {}
    if "trace_content" in value:
        import aws_sdk_iot_wireless.types.trace_content

        out["TraceContent"] = aws_sdk_iot_wireless.types.trace_content.serialize_json(
            value["trace_content"]
        )
    if "wireless_devices_to_add" in value:
        import aws_sdk_iot_wireless.types.wireless_device_list

        out["WirelessDevicesToAdd"] = (
            aws_sdk_iot_wireless.types.wireless_device_list.serialize_json(
                value["wireless_devices_to_add"]
            )
        )
    if "wireless_devices_to_remove" in value:
        import aws_sdk_iot_wireless.types.wireless_device_list

        out["WirelessDevicesToRemove"] = (
            aws_sdk_iot_wireless.types.wireless_device_list.serialize_json(
                value["wireless_devices_to_remove"]
            )
        )
    if "wireless_gateways_to_add" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_list

        out["WirelessGatewaysToAdd"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_list.serialize_json(
                value["wireless_gateways_to_add"]
            )
        )
    if "wireless_gateways_to_remove" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_list

        out["WirelessGatewaysToRemove"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_list.serialize_json(
                value["wireless_gateways_to_remove"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "multicast_groups_to_add" in value:
        import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list

        out["MulticastGroupsToAdd"] = (
            aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.serialize_json(
                value["multicast_groups_to_add"]
            )
        )
    if "multicast_groups_to_remove" in value:
        import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list

        out["MulticastGroupsToRemove"] = (
            aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.serialize_json(
                value["multicast_groups_to_remove"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkAnalyzerConfigurationRequest:
    out: UpdateNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TraceContent" in data:
        import aws_sdk_iot_wireless.types.trace_content

        out["trace_content"] = (
            aws_sdk_iot_wireless.types.trace_content.deserialize_json(
                data["TraceContent"]
            )
        )
    if "WirelessDevicesToAdd" in data:
        import aws_sdk_iot_wireless.types.wireless_device_list

        out["wireless_devices_to_add"] = (
            aws_sdk_iot_wireless.types.wireless_device_list.deserialize_json(
                data["WirelessDevicesToAdd"]
            )
        )
    if "WirelessDevicesToRemove" in data:
        import aws_sdk_iot_wireless.types.wireless_device_list

        out["wireless_devices_to_remove"] = (
            aws_sdk_iot_wireless.types.wireless_device_list.deserialize_json(
                data["WirelessDevicesToRemove"]
            )
        )
    if "WirelessGatewaysToAdd" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_list

        out["wireless_gateways_to_add"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_list.deserialize_json(
                data["WirelessGatewaysToAdd"]
            )
        )
    if "WirelessGatewaysToRemove" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_list

        out["wireless_gateways_to_remove"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_list.deserialize_json(
                data["WirelessGatewaysToRemove"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "MulticastGroupsToAdd" in data:
        import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list

        out["multicast_groups_to_add"] = (
            aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.deserialize_json(
                data["MulticastGroupsToAdd"]
            )
        )
    if "MulticastGroupsToRemove" in data:
        import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list

        out["multicast_groups_to_remove"] = (
            aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.deserialize_json(
                data["MulticastGroupsToRemove"]
            )
        )
    return out
