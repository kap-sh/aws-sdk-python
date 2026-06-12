"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeDeviceEc2Output``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.instance_summary_list

class DescribeDeviceEc2Output(TypedDict):
    instances: NotRequired["aws_sdk_snow_device_management.types.instance_summary_list.InstanceSummaryList"]
    """<p>A list of structures containing information about each instance. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceEc2Output) -> dict:
    out: dict = {}
    if "instances" in value:
        import aws_sdk_snow_device_management.types.instance_summary_list
        out["instances"] = aws_sdk_snow_device_management.types.instance_summary_list.serialize_json(value["instances"])
    return out


def deserialize_json(data: dict) -> DescribeDeviceEc2Output:
    out: DescribeDeviceEc2Output = {}  # type: ignore[typeddict-item]
    if "instances" in data:
        import aws_sdk_snow_device_management.types.instance_summary_list
        out["instances"] = aws_sdk_snow_device_management.types.instance_summary_list.deserialize_json(data["instances"])
    return out