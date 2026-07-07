"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DeviceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.managed_device_id
    import aws_sdk_snow_device_management.types.tag_map


class DeviceSummary(TypedDict, closed=True):
    managed_device_id: NotRequired[
        "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    ]
    """<p>The ID of the device.</p>"""
    managed_device_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    associated_with_job: NotRequired["str"]
    """<p>The ID of the job used to order the device.</p>"""
    tags: NotRequired["aws_sdk_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSummary) -> dict:
    out: dict = {}
    if "managed_device_id" in value:
        out["managedDeviceId"] = value["managed_device_id"]
    if "managed_device_arn" in value:
        out["managedDeviceArn"] = value["managed_device_arn"]
    if "associated_with_job" in value:
        out["associatedWithJob"] = value["associated_with_job"]
    if "tags" in value:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DeviceSummary:
    out: DeviceSummary = {}  # type: ignore[typeddict-item]
    if "managedDeviceId" in data:
        out["managed_device_id"] = data["managedDeviceId"]
    if "managedDeviceArn" in data:
        out["managed_device_arn"] = data["managedDeviceArn"]
    if "associatedWithJob" in data:
        out["associated_with_job"] = data["associatedWithJob"]
    if "tags" in data:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
