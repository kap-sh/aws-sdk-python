"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WebvttHlsSourceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.language_code


class WebvttHlsSourceSettings(TypedDict):
    rendition_group_id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. Specify alternative group ID"""
    rendition_language_code: NotRequired[
        "aws_sdk_mediaconvert.types.language_code.LanguageCode"
    ]
    """Optionally specify the language, using an ISO 639-2 or ISO 639-3 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code_list.php"""
    rendition_name: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. Specify media name"""


# --- restJson1 ser/de ---
def serialize_json(value: WebvttHlsSourceSettings) -> dict:
    out: dict = {}
    if "rendition_group_id" in value:
        out["renditionGroupId"] = value["rendition_group_id"]
    if "rendition_language_code" in value:
        import aws_sdk_mediaconvert.types.language_code

        out["renditionLanguageCode"] = (
            aws_sdk_mediaconvert.types.language_code.serialize_json(
                value["rendition_language_code"]
            )
        )
    if "rendition_name" in value:
        out["renditionName"] = value["rendition_name"]
    return out


def deserialize_json(data: dict) -> WebvttHlsSourceSettings:
    out: WebvttHlsSourceSettings = {}  # type: ignore[typeddict-item]
    if "renditionGroupId" in data:
        out["rendition_group_id"] = data["renditionGroupId"]
    if "renditionLanguageCode" in data:
        import aws_sdk_mediaconvert.types.language_code

        out["rendition_language_code"] = (
            aws_sdk_mediaconvert.types.language_code.deserialize_json(
                data["renditionLanguageCode"]
            )
        )
    if "renditionName" in data:
        out["rendition_name"] = data["renditionName"]
    return out
