"""Generated from Smithy shape ``com.amazonaws.medialive#HlsTimedMetadataScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class HlsTimedMetadataScheduleActionSettings(TypedDict, closed=True):
    id3: NotRequired["capo_medialive.types.__string.__string"]
    """Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: http://id3.org/id3v2.4.0-structure"""


# --- restJson1 ser/de ---
def serialize_json(value: HlsTimedMetadataScheduleActionSettings) -> dict:
    out: dict = {}
    if "id3" in value:
        out["id3"] = value["id3"]
    return out


def deserialize_json(data: dict) -> HlsTimedMetadataScheduleActionSettings:
    out: HlsTimedMetadataScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "id3" in data:
        out["id3"] = data["id3"]
    return out
