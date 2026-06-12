"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.device_summary

DeviceList: TypeAlias = list[
    "aws_sdk_workspaces_thin_client.types.device_summary.DeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceList) -> list:
    import aws_sdk_workspaces_thin_client.types.device_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_thin_client.types.device_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeviceList:
    import aws_sdk_workspaces_thin_client.types.device_summary

    out: DeviceList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_thin_client.types.device_summary.deserialize_json(item)
        )
    return out
