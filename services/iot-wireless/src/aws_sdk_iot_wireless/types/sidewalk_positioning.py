"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkPositioning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_name


class SidewalkPositioning(TypedDict, closed=True):
    destination_name: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The location destination name of the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkPositioning) -> dict:
    out: dict = {}
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    return out


def deserialize_json(data: dict) -> SidewalkPositioning:
    out: SidewalkPositioning = {}  # type: ignore[typeddict-item]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    return out
