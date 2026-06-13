"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeDeviceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_snow_device_management.types.capacity_list
    import aws_sdk_snow_device_management.types.managed_device_id
    import aws_sdk_snow_device_management.types.physical_network_interface_list
    import aws_sdk_snow_device_management.types.software_information
    import aws_sdk_snow_device_management.types.tag_map
    import aws_sdk_snow_device_management.types.unlock_state


class DescribeDeviceOutput(TypedDict):
    last_reached_out_at: NotRequired["datetime.datetime"]
    """<p>When the device last contacted the Amazon Web Services Cloud. Indicates that the device is online.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>When the device last pushed an update to the Amazon Web Services Cloud. Indicates when the device cache was refreshed.</p>"""
    tags: NotRequired["aws_sdk_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>"""
    managed_device_id: NotRequired[
        "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    ]
    """<p>The ID of the device that you checked the information for.</p>"""
    managed_device_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    device_type: NotRequired["str"]
    """<p>The type of Amazon Web Services Snow Family device.</p>"""
    associated_with_job: NotRequired["str"]
    """<p>The ID of the job used when ordering the device.</p>"""
    device_state: NotRequired[
        "aws_sdk_snow_device_management.types.unlock_state.UnlockState"
    ]
    """<p>The current state of the device.</p>"""
    physical_network_interfaces: NotRequired[
        "aws_sdk_snow_device_management.types.physical_network_interface_list.PhysicalNetworkInterfaceList"
    ]
    """<p>The network interfaces available on the device.</p>"""
    device_capacities: NotRequired[
        "aws_sdk_snow_device_management.types.capacity_list.CapacityList"
    ]
    """<p>The hardware specifications of the device. </p>"""
    software: NotRequired[
        "aws_sdk_snow_device_management.types.software_information.SoftwareInformation"
    ]
    """<p>The software installed on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceOutput) -> dict:
    out: dict = {}
    if "last_reached_out_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["lastReachedOutAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["last_reached_out_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "tags" in value:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.serialize_json(
            value["tags"]
        )
    if "managed_device_id" in value:
        out["managedDeviceId"] = value["managed_device_id"]
    if "managed_device_arn" in value:
        out["managedDeviceArn"] = value["managed_device_arn"]
    if "device_type" in value:
        out["deviceType"] = value["device_type"]
    if "associated_with_job" in value:
        out["associatedWithJob"] = value["associated_with_job"]
    if "device_state" in value:
        out["deviceState"] = value["device_state"]
    if "physical_network_interfaces" in value:
        import aws_sdk_snow_device_management.types.physical_network_interface_list

        out["physicalNetworkInterfaces"] = (
            aws_sdk_snow_device_management.types.physical_network_interface_list.serialize_json(
                value["physical_network_interfaces"]
            )
        )
    if "device_capacities" in value:
        import aws_sdk_snow_device_management.types.capacity_list

        out["deviceCapacities"] = (
            aws_sdk_snow_device_management.types.capacity_list.serialize_json(
                value["device_capacities"]
            )
        )
    if "software" in value:
        import aws_sdk_snow_device_management.types.software_information

        out["software"] = (
            aws_sdk_snow_device_management.types.software_information.serialize_json(
                value["software"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDeviceOutput:
    out: DescribeDeviceOutput = {}  # type: ignore[typeddict-item]
    if "lastReachedOutAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["last_reached_out_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["lastReachedOutAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "tags" in data:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "managedDeviceId" in data:
        out["managed_device_id"] = data["managedDeviceId"]
    if "managedDeviceArn" in data:
        out["managed_device_arn"] = data["managedDeviceArn"]
    if "deviceType" in data:
        out["device_type"] = data["deviceType"]
    if "associatedWithJob" in data:
        out["associated_with_job"] = data["associatedWithJob"]
    if "deviceState" in data:
        out["device_state"] = data["deviceState"]
    if "physicalNetworkInterfaces" in data:
        import aws_sdk_snow_device_management.types.physical_network_interface_list

        out["physical_network_interfaces"] = (
            aws_sdk_snow_device_management.types.physical_network_interface_list.deserialize_json(
                data["physicalNetworkInterfaces"]
            )
        )
    if "deviceCapacities" in data:
        import aws_sdk_snow_device_management.types.capacity_list

        out["device_capacities"] = (
            aws_sdk_snow_device_management.types.capacity_list.deserialize_json(
                data["deviceCapacities"]
            )
        )
    if "software" in data:
        import aws_sdk_snow_device_management.types.software_information

        out["software"] = (
            aws_sdk_snow_device_management.types.software_information.deserialize_json(
                data["software"]
            )
        )
    return out
