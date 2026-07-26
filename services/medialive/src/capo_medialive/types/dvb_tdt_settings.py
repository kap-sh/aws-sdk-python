"""Generated from Smithy shape ``com.amazonaws.medialive#DvbTdtSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1000_max30000


class DvbTdtSettings(TypedDict, closed=True):
    rep_interval: NotRequired[
        "capo_medialive.types.__integer_min1000_max30000.__integerMin1000Max30000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbTdtSettings) -> dict:
    out: dict = {}
    if "rep_interval" in value:
        out["repInterval"] = value["rep_interval"]
    return out


def deserialize_json(data: dict) -> DvbTdtSettings:
    out: DvbTdtSettings = {}  # type: ignore[typeddict-item]
    if "repInterval" in data:
        out["rep_interval"] = data["repInterval"]
    return out
