"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__string


class SdiSourceMapping(TypedDict):
    card_number: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """A number that uniquely identifies the SDI card on the node hardware."""
    channel_number: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """A number that uniquely identifies a port on the SDI card."""
    sdi_source: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the SdiSource to associate with this port on this card. You can use the ListSdiSources operation to discover all the IDs."""


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMapping) -> dict:
    out: dict = {}
    if "card_number" in value:
        out["cardNumber"] = value["card_number"]
    if "channel_number" in value:
        out["channelNumber"] = value["channel_number"]
    if "sdi_source" in value:
        out["sdiSource"] = value["sdi_source"]
    return out


def deserialize_json(data: dict) -> SdiSourceMapping:
    out: SdiSourceMapping = {}  # type: ignore[typeddict-item]
    if "cardNumber" in data:
        out["card_number"] = data["cardNumber"]
    if "channelNumber" in data:
        out["channel_number"] = data["channelNumber"]
    if "sdiSource" in data:
        out["sdi_source"] = data["sdiSource"]
    return out
