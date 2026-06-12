"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.alternate_softwares
    import aws_sdk_panorama.types.created_time
    import aws_sdk_panorama.types.current_software
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.device_aggregated_status
    import aws_sdk_panorama.types.device_arn
    import aws_sdk_panorama.types.device_brand
    import aws_sdk_panorama.types.device_connection_status
    import aws_sdk_panorama.types.device_id
    import aws_sdk_panorama.types.device_name
    import aws_sdk_panorama.types.device_serial_number
    import aws_sdk_panorama.types.device_status
    import aws_sdk_panorama.types.device_type
    import aws_sdk_panorama.types.latest_alternate_software
    import aws_sdk_panorama.types.latest_device_job
    import aws_sdk_panorama.types.latest_software
    import aws_sdk_panorama.types.lease_expiration_time
    import aws_sdk_panorama.types.network_payload
    import aws_sdk_panorama.types.network_status
    import aws_sdk_panorama.types.tag_map


class DescribeDeviceResponse(TypedDict):
    device_id: NotRequired["aws_sdk_panorama.types.device_id.DeviceId"]
    """<p>The device's ID.</p>"""
    name: NotRequired["aws_sdk_panorama.types.device_name.DeviceName"]
    """<p>The device's name.</p>"""
    arn: NotRequired["aws_sdk_panorama.types.device_arn.DeviceArn"]
    """<p>The device's ARN.</p>"""
    description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>The device's description.</p>"""
    type: NotRequired["aws_sdk_panorama.types.device_type.DeviceType"]
    """<p>The device's type.</p>"""
    device_connection_status: NotRequired[
        "aws_sdk_panorama.types.device_connection_status.DeviceConnectionStatus"
    ]
    """<p>The device's connection status.</p>"""
    created_time: NotRequired["aws_sdk_panorama.types.created_time.CreatedTime"]
    """<p>When the device was created.</p>"""
    provisioning_status: NotRequired[
        "aws_sdk_panorama.types.device_status.DeviceStatus"
    ]
    """<p>The device's provisioning status.</p>"""
    latest_software: NotRequired[
        "aws_sdk_panorama.types.latest_software.LatestSoftware"
    ]
    """<p>The latest software version available for the device.</p>"""
    current_software: NotRequired[
        "aws_sdk_panorama.types.current_software.CurrentSoftware"
    ]
    """<p>The device's current software version.</p>"""
    serial_number: NotRequired[
        "aws_sdk_panorama.types.device_serial_number.DeviceSerialNumber"
    ]
    """<p>The device's serial number.</p>"""
    tags: NotRequired["aws_sdk_panorama.types.tag_map.TagMap"]
    """<p>The device's tags.</p>"""
    networking_configuration: NotRequired[
        "aws_sdk_panorama.types.network_payload.NetworkPayload"
    ]
    """<p>The device's networking configuration.</p>"""
    current_networking_status: NotRequired[
        "aws_sdk_panorama.types.network_status.NetworkStatus"
    ]
    """<p>The device's networking status.</p>"""
    lease_expiration_time: NotRequired[
        "aws_sdk_panorama.types.lease_expiration_time.LeaseExpirationTime"
    ]
    """<p>The device's lease expiration time.</p>"""
    alternate_softwares: NotRequired[
        "aws_sdk_panorama.types.alternate_softwares.AlternateSoftwares"
    ]
    """<p>Beta software releases available for the device.</p>"""
    latest_alternate_software: NotRequired[
        "aws_sdk_panorama.types.latest_alternate_software.LatestAlternateSoftware"
    ]
    """<p>The most recent beta software release.</p>"""
    brand: NotRequired["aws_sdk_panorama.types.device_brand.DeviceBrand"]
    """<p>The device's maker.</p>"""
    latest_device_job: NotRequired[
        "aws_sdk_panorama.types.latest_device_job.LatestDeviceJob"
    ]
    """<p>A device's latest job. Includes the target image version, and the job status.</p>"""
    device_aggregated_status: NotRequired[
        "aws_sdk_panorama.types.device_aggregated_status.DeviceAggregatedStatus"
    ]
    """<p>A device's aggregated status. Including the device's connection status, provisioning status, and lease status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceResponse) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "device_connection_status" in value:
        out["DeviceConnectionStatus"] = value["device_connection_status"]
    if "created_time" in value:
        import aws_sdk_panorama.types.created_time

        out["CreatedTime"] = aws_sdk_panorama.types.created_time.serialize_json(
            value["created_time"]
        )
    if "provisioning_status" in value:
        out["ProvisioningStatus"] = value["provisioning_status"]
    if "latest_software" in value:
        out["LatestSoftware"] = value["latest_software"]
    if "current_software" in value:
        out["CurrentSoftware"] = value["current_software"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "tags" in value:
        import aws_sdk_panorama.types.tag_map

        out["Tags"] = aws_sdk_panorama.types.tag_map.serialize_json(value["tags"])
    if "networking_configuration" in value:
        import aws_sdk_panorama.types.network_payload

        out["NetworkingConfiguration"] = (
            aws_sdk_panorama.types.network_payload.serialize_json(
                value["networking_configuration"]
            )
        )
    if "current_networking_status" in value:
        import aws_sdk_panorama.types.network_status

        out["CurrentNetworkingStatus"] = (
            aws_sdk_panorama.types.network_status.serialize_json(
                value["current_networking_status"]
            )
        )
    if "lease_expiration_time" in value:
        import aws_sdk_panorama.types.lease_expiration_time

        out["LeaseExpirationTime"] = (
            aws_sdk_panorama.types.lease_expiration_time.serialize_json(
                value["lease_expiration_time"]
            )
        )
    if "alternate_softwares" in value:
        import aws_sdk_panorama.types.alternate_softwares

        out["AlternateSoftwares"] = (
            aws_sdk_panorama.types.alternate_softwares.serialize_json(
                value["alternate_softwares"]
            )
        )
    if "latest_alternate_software" in value:
        out["LatestAlternateSoftware"] = value["latest_alternate_software"]
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "latest_device_job" in value:
        import aws_sdk_panorama.types.latest_device_job

        out["LatestDeviceJob"] = (
            aws_sdk_panorama.types.latest_device_job.serialize_json(
                value["latest_device_job"]
            )
        )
    if "device_aggregated_status" in value:
        out["DeviceAggregatedStatus"] = value["device_aggregated_status"]
    return out


def deserialize_json(data: dict) -> DescribeDeviceResponse:
    out: DescribeDeviceResponse = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "DeviceConnectionStatus" in data:
        out["device_connection_status"] = data["DeviceConnectionStatus"]
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.created_time

        out["created_time"] = aws_sdk_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    if "ProvisioningStatus" in data:
        out["provisioning_status"] = data["ProvisioningStatus"]
    if "LatestSoftware" in data:
        out["latest_software"] = data["LatestSoftware"]
    if "CurrentSoftware" in data:
        out["current_software"] = data["CurrentSoftware"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "Tags" in data:
        import aws_sdk_panorama.types.tag_map

        out["tags"] = aws_sdk_panorama.types.tag_map.deserialize_json(data["Tags"])
    if "NetworkingConfiguration" in data:
        import aws_sdk_panorama.types.network_payload

        out["networking_configuration"] = (
            aws_sdk_panorama.types.network_payload.deserialize_json(
                data["NetworkingConfiguration"]
            )
        )
    if "CurrentNetworkingStatus" in data:
        import aws_sdk_panorama.types.network_status

        out["current_networking_status"] = (
            aws_sdk_panorama.types.network_status.deserialize_json(
                data["CurrentNetworkingStatus"]
            )
        )
    if "LeaseExpirationTime" in data:
        import aws_sdk_panorama.types.lease_expiration_time

        out["lease_expiration_time"] = (
            aws_sdk_panorama.types.lease_expiration_time.deserialize_json(
                data["LeaseExpirationTime"]
            )
        )
    if "AlternateSoftwares" in data:
        import aws_sdk_panorama.types.alternate_softwares

        out["alternate_softwares"] = (
            aws_sdk_panorama.types.alternate_softwares.deserialize_json(
                data["AlternateSoftwares"]
            )
        )
    if "LatestAlternateSoftware" in data:
        out["latest_alternate_software"] = data["LatestAlternateSoftware"]
    if "Brand" in data:
        out["brand"] = data["Brand"]
    if "LatestDeviceJob" in data:
        import aws_sdk_panorama.types.latest_device_job

        out["latest_device_job"] = (
            aws_sdk_panorama.types.latest_device_job.deserialize_json(
                data["LatestDeviceJob"]
            )
        )
    if "DeviceAggregatedStatus" in data:
        out["device_aggregated_status"] = data["DeviceAggregatedStatus"]
    return out
