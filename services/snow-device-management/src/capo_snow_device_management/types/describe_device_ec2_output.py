"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeDeviceEc2Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.instance_summary_list


class DescribeDeviceEc2Output(TypedDict, closed=True):
    instances: NotRequired[
        "capo_snow_device_management.types.instance_summary_list.InstanceSummaryList"
    ]
    """<p>A list of structures containing information about each instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceEc2Output) -> dict:
    out: dict = {}
    if "instances" in value:
        import capo_snow_device_management.types.instance_summary_list

        out["instances"] = (
            capo_snow_device_management.types.instance_summary_list.serialize_json(
                value["instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDeviceEc2Output:
    out: DescribeDeviceEc2Output = {}  # type: ignore[typeddict-item]
    if "instances" in data:
        import capo_snow_device_management.types.instance_summary_list

        out["instances"] = (
            capo_snow_device_management.types.instance_summary_list.deserialize_json(
                data["instances"]
            )
        )
    return out
