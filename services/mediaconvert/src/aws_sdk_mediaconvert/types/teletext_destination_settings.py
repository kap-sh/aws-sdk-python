"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TeletextDestinationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_teletext_page_type
    import aws_sdk_mediaconvert.types.__string_min3_max3_pattern1809a_faf09a_eae


class TeletextDestinationSettings(TypedDict):
    page_number: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min3_max3_pattern1809a_faf09a_eae.__stringMin3Max3Pattern1809aFAF09aEAE"
    ]
    """Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field."""
    page_types: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_teletext_page_type.__listOfTeletextPageType"
    ]
    """Specify the page types for this Teletext page. If you don't specify a value here, the service sets the page type to the default value Subtitle. If you pass through the entire set of Teletext data, don't use this field. When you pass through a set of Teletext pages, your output has the same page types as your input."""


# --- restJson1 ser/de ---
def serialize_json(value: TeletextDestinationSettings) -> dict:
    out: dict = {}
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    if "page_types" in value:
        import aws_sdk_mediaconvert.types.__list_of_teletext_page_type

        out["pageTypes"] = (
            aws_sdk_mediaconvert.types.__list_of_teletext_page_type.serialize_json(
                value["page_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> TeletextDestinationSettings:
    out: TeletextDestinationSettings = {}  # type: ignore[typeddict-item]
    if "pageNumber" in data:
        out["page_number"] = data["pageNumber"]
    if "pageTypes" in data:
        import aws_sdk_mediaconvert.types.__list_of_teletext_page_type

        out["page_types"] = (
            aws_sdk_mediaconvert.types.__list_of_teletext_page_type.deserialize_json(
                data["pageTypes"]
            )
        )
    return out
