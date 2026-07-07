"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkGetStartImportInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_creation_file_list
    import aws_sdk_iot_wireless.types.role
    import aws_sdk_iot_wireless.types.sidewalk_positioning


class SidewalkGetStartImportInfo(TypedDict, closed=True):
    device_creation_file_list: NotRequired[
        "aws_sdk_iot_wireless.types.device_creation_file_list.DeviceCreationFileList"
    ]
    """<p>List of Sidewalk devices that are added to the import task.</p>"""
    role: NotRequired["aws_sdk_iot_wireless.types.role.Role"]
    """<p>The IAM role that allows AWS IoT Wireless to access the CSV file in the S3 bucket.</p>"""
    positioning: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkGetStartImportInfo) -> dict:
    out: dict = {}
    if "device_creation_file_list" in value:
        import aws_sdk_iot_wireless.types.device_creation_file_list

        out["DeviceCreationFileList"] = (
            aws_sdk_iot_wireless.types.device_creation_file_list.serialize_json(
                value["device_creation_file_list"]
            )
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            aws_sdk_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkGetStartImportInfo:
    out: SidewalkGetStartImportInfo = {}  # type: ignore[typeddict-item]
    if "DeviceCreationFileList" in data:
        import aws_sdk_iot_wireless.types.device_creation_file_list

        out["device_creation_file_list"] = (
            aws_sdk_iot_wireless.types.device_creation_file_list.deserialize_json(
                data["DeviceCreationFileList"]
            )
        )
    if "Role" in data:
        out["role"] = data["Role"]
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            aws_sdk_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    return out
