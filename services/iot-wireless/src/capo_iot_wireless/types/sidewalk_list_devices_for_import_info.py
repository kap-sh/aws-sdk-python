"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkListDevicesForImportInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.sidewalk_positioning


class SidewalkListDevicesForImportInfo(TypedDict, closed=True):
    positioning: NotRequired[
        "capo_iot_wireless.types.sidewalk_positioning.SidewalkPositioning"
    ]
    """<p>The Positioning object of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkListDevicesForImportInfo) -> dict:
    out: dict = {}
    if "positioning" in value:
        import capo_iot_wireless.types.sidewalk_positioning

        out["Positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkListDevicesForImportInfo:
    out: SidewalkListDevicesForImportInfo = {}  # type: ignore[typeddict-item]
    if "Positioning" in data:
        import capo_iot_wireless.types.sidewalk_positioning

        out["positioning"] = (
            capo_iot_wireless.types.sidewalk_positioning.deserialize_json(
                data["Positioning"]
            )
        )
    return out
