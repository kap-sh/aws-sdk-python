"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbTdtSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1000_max30000


class DvbTdtSettings(TypedDict, closed=True):
    tdt_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min1000_max30000.__integerMin1000Max30000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbTdtSettings) -> dict:
    out: dict = {}
    if "tdt_interval" in value:
        out["tdtInterval"] = value["tdt_interval"]
    return out


def deserialize_json(data: dict) -> DvbTdtSettings:
    out: DvbTdtSettings = {}  # type: ignore[typeddict-item]
    if "tdtInterval" in data:
        out["tdt_interval"] = data["tdtInterval"]
    return out
