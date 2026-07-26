"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TeletextDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_teletext_page_type
    import capo_mediaconvert.types.__string_min3_max3_pattern1809a_faf09a_eae


class TeletextDestinationSettings(TypedDict, closed=True):
    page_number: NotRequired[
        "capo_mediaconvert.types.__string_min3_max3_pattern1809a_faf09a_eae.__stringMin3Max3Pattern1809aFAF09aEAE"
    ]
    """Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field."""
    page_types: NotRequired[
        "capo_mediaconvert.types.__list_of_teletext_page_type.__listOfTeletextPageType"
    ]
    """Specify the page types for this Teletext page. If you don't specify a value here, the service sets the page type to the default value Subtitle. If you pass through the entire set of Teletext data, don't use this field. When you pass through a set of Teletext pages, your output has the same page types as your input."""


# --- restJson1 ser/de ---
def serialize_json(value: TeletextDestinationSettings) -> dict:
    out: dict = {}
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    if "page_types" in value:
        import capo_mediaconvert.types.__list_of_teletext_page_type

        out["pageTypes"] = (
            capo_mediaconvert.types.__list_of_teletext_page_type.serialize_json(
                value["page_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> TeletextDestinationSettings:
    out: TeletextDestinationSettings = {}  # type: ignore[typeddict-item]
    if "pageNumber" in data:
        out["page_number"] = data["pageNumber"]
    if "pageTypes" in data:
        import capo_mediaconvert.types.__list_of_teletext_page_type

        out["page_types"] = (
            capo_mediaconvert.types.__list_of_teletext_page_type.deserialize_json(
                data["pageTypes"]
            )
        )
    return out
