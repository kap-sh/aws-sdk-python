"""Generated from Smithy shape ``com.amazonaws.iotwireless#ImportedWirelessDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.imported_sidewalk_device


class ImportedWirelessDevice(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.imported_sidewalk_device.ImportedSidewalkDevice"
    ]
    """<p>The Sidewalk-related information about a device that has been added to an import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportedWirelessDevice) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.imported_sidewalk_device

        out["Sidewalk"] = (
            capo_iot_wireless.types.imported_sidewalk_device.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportedWirelessDevice:
    out: ImportedWirelessDevice = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.imported_sidewalk_device

        out["sidewalk"] = (
            capo_iot_wireless.types.imported_sidewalk_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
