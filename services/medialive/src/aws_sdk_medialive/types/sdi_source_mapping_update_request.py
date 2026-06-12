"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMappingUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__string


class SdiSourceMappingUpdateRequest(TypedDict):
    card_number: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """A number that uniquely identifies the SDI card on the node hardware. For information about how physical cards are identified on your node hardware, see the documentation for your node hardware. The numbering always starts at 1."""
    channel_number: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """A number that uniquely identifies a port on the card. This must be an SDI port (not a timecode port, for example). For information about how ports are identified on physical cards, see the documentation for your node hardware."""
    sdi_source: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of a SDI source streaming on the given SDI capture card port."""


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMappingUpdateRequest) -> dict:
    out: dict = {}
    if "card_number" in value:
        out["cardNumber"] = value["card_number"]
    if "channel_number" in value:
        out["channelNumber"] = value["channel_number"]
    if "sdi_source" in value:
        out["sdiSource"] = value["sdi_source"]
    return out


def deserialize_json(data: dict) -> SdiSourceMappingUpdateRequest:
    out: SdiSourceMappingUpdateRequest = {}  # type: ignore[typeddict-item]
    if "cardNumber" in data:
        out["card_number"] = data["cardNumber"]
    if "channelNumber" in data:
        out["channel_number"] = data["channelNumber"]
    if "sdiSource" in data:
        out["sdi_source"] = data["sdiSource"]
    return out
