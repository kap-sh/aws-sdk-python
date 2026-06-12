"""Generated from Smithy shape ``com.amazonaws.medialive#AncillarySourceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1_max4


class AncillarySourceSettings(TypedDict):
    source_ancillary_channel_number: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """Specifies the number (1 to 4) of the captions channel you want to extract from the ancillary captions. If you plan to convert the ancillary captions to another format, complete this field. If you plan to choose Embedded as the captions destination in the output (to pass through all the channels in the ancillary captions), leave this field blank because MediaLive ignores the field."""


# --- restJson1 ser/de ---
def serialize_json(value: AncillarySourceSettings) -> dict:
    out: dict = {}
    if "source_ancillary_channel_number" in value:
        out["sourceAncillaryChannelNumber"] = value["source_ancillary_channel_number"]
    return out


def deserialize_json(data: dict) -> AncillarySourceSettings:
    out: AncillarySourceSettings = {}  # type: ignore[typeddict-item]
    if "sourceAncillaryChannelNumber" in data:
        out["source_ancillary_channel_number"] = data["sourceAncillaryChannelNumber"]
    return out
