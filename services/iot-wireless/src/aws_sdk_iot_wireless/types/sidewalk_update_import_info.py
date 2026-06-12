"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkUpdateImportInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_creation_file


class SidewalkUpdateImportInfo(TypedDict):
    device_creation_file: NotRequired[
        "aws_sdk_iot_wireless.types.device_creation_file.DeviceCreationFile"
    ]
    """<p>The CSV file contained in an S3 bucket that's used for appending devices to an existing import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkUpdateImportInfo) -> dict:
    out: dict = {}
    if "device_creation_file" in value:
        out["DeviceCreationFile"] = value["device_creation_file"]
    return out


def deserialize_json(data: dict) -> SidewalkUpdateImportInfo:
    out: SidewalkUpdateImportInfo = {}  # type: ignore[typeddict-item]
    if "DeviceCreationFile" in data:
        out["device_creation_file"] = data["DeviceCreationFile"]
    return out
