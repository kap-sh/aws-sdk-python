"""Generated from Smithy shape ``com.amazonaws.medialive#DvbNitSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max65536
    import capo_medialive.types.__integer_min25_max10000
    import capo_medialive.types.__string_min1_max256


class DvbNitSettings(TypedDict, closed=True):
    network_id: NotRequired[
        "capo_medialive.types.__integer_min0_max65536.__integerMin0Max65536"
    ]
    """The numeric value placed in the Network Information Table (NIT)."""
    network_name: NotRequired[
        "capo_medialive.types.__string_min1_max256.__stringMin1Max256"
    ]
    """The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters."""
    rep_interval: NotRequired[
        "capo_medialive.types.__integer_min25_max10000.__integerMin25Max10000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbNitSettings) -> dict:
    out: dict = {}
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "network_name" in value:
        out["networkName"] = value["network_name"]
    if "rep_interval" in value:
        out["repInterval"] = value["rep_interval"]
    return out


def deserialize_json(data: dict) -> DvbNitSettings:
    out: DvbNitSettings = {}  # type: ignore[typeddict-item]
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    if "repInterval" in data:
        out["rep_interval"] = data["repInterval"]
    return out
