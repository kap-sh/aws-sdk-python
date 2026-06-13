"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListDevicesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.device_summary_list
    import aws_sdk_snow_device_management.types.next_token


class ListDevicesOutput(TypedDict):
    devices: NotRequired[
        "aws_sdk_snow_device_management.types.device_summary_list.DeviceSummaryList"
    ]
    """<p>A list of device structures that contain information about the device.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesOutput) -> dict:
    out: dict = {}
    if "devices" in value:
        import aws_sdk_snow_device_management.types.device_summary_list

        out["devices"] = (
            aws_sdk_snow_device_management.types.device_summary_list.serialize_json(
                value["devices"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevicesOutput:
    out: ListDevicesOutput = {}  # type: ignore[typeddict-item]
    if "devices" in data:
        import aws_sdk_snow_device_management.types.device_summary_list

        out["devices"] = (
            aws_sdk_snow_device_management.types.device_summary_list.deserialize_json(
                data["devices"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
