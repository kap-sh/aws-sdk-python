"""Generated from Smithy shape ``com.amazonaws.panorama#Device``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.created_time
    import capo_panorama.types.current_software
    import capo_panorama.types.description
    import capo_panorama.types.device_aggregated_status
    import capo_panorama.types.device_brand
    import capo_panorama.types.device_id
    import capo_panorama.types.device_name
    import capo_panorama.types.device_status
    import capo_panorama.types.device_type
    import capo_panorama.types.last_updated_time
    import capo_panorama.types.latest_device_job
    import capo_panorama.types.lease_expiration_time
    import capo_panorama.types.tag_map


class Device(TypedDict, closed=True):
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>The device's ID.</p>"""
    name: NotRequired["capo_panorama.types.device_name.DeviceName"]
    """<p>The device's name.</p>"""
    created_time: NotRequired["capo_panorama.types.created_time.CreatedTime"]
    """<p>When the device was created.</p>"""
    provisioning_status: NotRequired["capo_panorama.types.device_status.DeviceStatus"]
    """<p>The device's provisioning status.</p>"""
    last_updated_time: NotRequired[
        "capo_panorama.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>When the device was updated.</p>"""
    lease_expiration_time: NotRequired[
        "capo_panorama.types.lease_expiration_time.LeaseExpirationTime"
    ]
    """<p>The device's lease expiration time.</p>"""
    brand: NotRequired["capo_panorama.types.device_brand.DeviceBrand"]
    """<p>The device's maker.</p>"""
    current_software: NotRequired[
        "capo_panorama.types.current_software.CurrentSoftware"
    ]
    """<p>A device's current software.</p>"""
    description: NotRequired["capo_panorama.types.description.Description"]
    """<p>A description for the device.</p>"""
    tags: NotRequired["capo_panorama.types.tag_map.TagMap"]
    """<p>The device's tags.</p>"""
    type: NotRequired["capo_panorama.types.device_type.DeviceType"]
    """<p>The device's type.</p>"""
    latest_device_job: NotRequired[
        "capo_panorama.types.latest_device_job.LatestDeviceJob"
    ]
    """<p>A device's latest job. Includes the target image version, and the update job status.</p>"""
    device_aggregated_status: NotRequired[
        "capo_panorama.types.device_aggregated_status.DeviceAggregatedStatus"
    ]
    """<p>A device's aggregated status. Including the device's connection status, provisioning status, and lease status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time" in value:
        import capo_panorama.types.created_time

        out["CreatedTime"] = capo_panorama.types.created_time.serialize_json(
            value["created_time"]
        )
    if "provisioning_status" in value:
        out["ProvisioningStatus"] = value["provisioning_status"]
    if "last_updated_time" in value:
        import capo_panorama.types.last_updated_time

        out["LastUpdatedTime"] = capo_panorama.types.last_updated_time.serialize_json(
            value["last_updated_time"]
        )
    if "lease_expiration_time" in value:
        import capo_panorama.types.lease_expiration_time

        out["LeaseExpirationTime"] = (
            capo_panorama.types.lease_expiration_time.serialize_json(
                value["lease_expiration_time"]
            )
        )
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "current_software" in value:
        out["CurrentSoftware"] = value["current_software"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_panorama.types.tag_map

        out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    if "type" in value:
        out["Type"] = value["type"]
    if "latest_device_job" in value:
        import capo_panorama.types.latest_device_job

        out["LatestDeviceJob"] = capo_panorama.types.latest_device_job.serialize_json(
            value["latest_device_job"]
        )
    if "device_aggregated_status" in value:
        out["DeviceAggregatedStatus"] = value["device_aggregated_status"]
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTime" in data:
        import capo_panorama.types.created_time

        out["created_time"] = capo_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    if "ProvisioningStatus" in data:
        out["provisioning_status"] = data["ProvisioningStatus"]
    if "LastUpdatedTime" in data:
        import capo_panorama.types.last_updated_time

        out["last_updated_time"] = (
            capo_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if "LeaseExpirationTime" in data:
        import capo_panorama.types.lease_expiration_time

        out["lease_expiration_time"] = (
            capo_panorama.types.lease_expiration_time.deserialize_json(
                data["LeaseExpirationTime"]
            )
        )
    if "Brand" in data:
        out["brand"] = data["Brand"]
    if "CurrentSoftware" in data:
        out["current_software"] = data["CurrentSoftware"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    if "Type" in data:
        out["type"] = data["Type"]
    if "LatestDeviceJob" in data:
        import capo_panorama.types.latest_device_job

        out["latest_device_job"] = (
            capo_panorama.types.latest_device_job.deserialize_json(
                data["LatestDeviceJob"]
            )
        )
    if "DeviceAggregatedStatus" in data:
        out["device_aggregated_status"] = data["DeviceAggregatedStatus"]
    return out
