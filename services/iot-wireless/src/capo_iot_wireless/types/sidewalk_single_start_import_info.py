"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkSingleStartImportInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.sidewalk_manufacturing_sn
    import capo_iot_wireless.types.sidewalk_positioning


class SidewalkSingleStartImportInfo(TypedDict, closed=True):
    sidewalk_manufacturing_sn: NotRequired[
        "capo_iot_wireless.types.sidewalk_manufacturing_sn.SidewalkManufacturingSn"
    ]
    """<p>The Sidewalk manufacturing serial number (SMSN) of the device added to the import task.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkSingleStartImportInfo) -> dict:
    out: dict = {}
    if "sidewalk_manufacturing_sn" in value:
        out["SidewalkManufacturingSn"] = value["sidewalk_manufacturing_sn"]
    if "positioning" in value:
        import capo_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkSingleStartImportInfo:
    out: SidewalkSingleStartImportInfo = {}  # type: ignore[typeddict-item]
    if "SidewalkManufacturingSn" in data:
        out["sidewalk_manufacturing_sn"] = data["SidewalkManufacturingSn"]
    if "Positioning" in data:
        import capo_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    return out
