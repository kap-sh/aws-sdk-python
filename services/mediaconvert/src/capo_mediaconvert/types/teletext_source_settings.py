"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TeletextSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_min3_max3_pattern1809a_faf09a_eae


class TeletextSourceSettings(TypedDict, closed=True):
    page_number: NotRequired[
        "capo_mediaconvert.types.__string_min3_max3_pattern1809a_faf09a_eae.__stringMin3Max3Pattern1809aFAF09aEAE"
    ]
    """Use Page Number to specify the three-digit hexadecimal page number that will be used for Teletext captions. Do not use this setting if you are passing through teletext from the input source to output."""


# --- restJson1 ser/de ---
def serialize_json(value: TeletextSourceSettings) -> dict:
    out: dict = {}
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    return out


def deserialize_json(data: dict) -> TeletextSourceSettings:
    out: TeletextSourceSettings = {}  # type: ignore[typeddict-item]
    if "pageNumber" in data:
        out["page_number"] = data["pageNumber"]
    return out
