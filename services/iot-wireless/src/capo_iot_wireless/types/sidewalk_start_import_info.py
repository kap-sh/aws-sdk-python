"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkStartImportInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_creation_file
    import capo_iot_wireless.types.role
    import capo_iot_wireless.types.sidewalk_positioning


class SidewalkStartImportInfo(TypedDict, closed=True):
    device_creation_file: NotRequired[
        "capo_iot_wireless.types.device_creation_file.DeviceCreationFile"
    ]
    """<p>The CSV file contained in an S3 bucket that's used for adding devices to an import task.</p>"""
    role: NotRequired["capo_iot_wireless.types.role.Role"]
    """<p>The IAM role that allows AWS IoT Wireless to access the CSV file in the S3 bucket.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkStartImportInfo) -> dict:
    out: dict = {}
    if "device_creation_file" in value:
        out["DeviceCreationFile"] = value["device_creation_file"]
    if "role" in value:
        out["Role"] = value["role"]
    if "positioning" in value:
        import capo_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkStartImportInfo:
    out: SidewalkStartImportInfo = {}  # type: ignore[typeddict-item]
    if "DeviceCreationFile" in data:
        out["device_creation_file"] = data["DeviceCreationFile"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "Positioning" in data:
        import capo_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    return out
