"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeDeviceEc2Input``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_snow_device_management.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.instance_ids_list
    import aws_sdk_snow_device_management.types.managed_device_id


class DescribeDeviceEc2Input(TypedDict, closed=True):
    managed_device_id: (
        "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    )
    """<p>The ID of the managed device.</p>"""
    instance_ids: (
        "aws_sdk_snow_device_management.types.instance_ids_list.InstanceIdsList"
    )
    """<p>A list of instance IDs associated with the managed device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceEc2Input) -> dict:
    out: dict = {}
    import aws_sdk_snow_device_management.types.instance_ids_list

    out["instanceIds"] = (
        aws_sdk_snow_device_management.types.instance_ids_list.serialize_json(
            value["instance_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeDeviceEc2Input:
    out: DescribeDeviceEc2Input = {}  # type: ignore[typeddict-item]
    if "instanceIds" in data:
        import aws_sdk_snow_device_management.types.instance_ids_list

        out["instance_ids"] = (
            aws_sdk_snow_device_management.types.instance_ids_list.deserialize_json(
                data["instanceIds"]
            )
        )
    else:
        raise DeserializationError("DescribeDeviceEc2Input.instance_ids required")
    return out
