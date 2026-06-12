"""Generated from Smithy shape ``com.amazonaws.iotwireless#ImportedWirelessDevice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.imported_sidewalk_device


class ImportedWirelessDevice(TypedDict):
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.imported_sidewalk_device.ImportedSidewalkDevice"
    ]
    """<p>The Sidewalk-related information about a device that has been added to an import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportedWirelessDevice) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.imported_sidewalk_device

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.imported_sidewalk_device.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportedWirelessDevice:
    out: ImportedWirelessDevice = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.imported_sidewalk_device

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.imported_sidewalk_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
