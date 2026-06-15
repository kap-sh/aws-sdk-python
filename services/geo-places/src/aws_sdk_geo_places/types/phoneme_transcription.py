"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeTranscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.language_tag
    import aws_sdk_geo_places.types.sensitive_boolean
    import aws_sdk_geo_places.types.sensitive_string


class PhonemeTranscription(TypedDict):
    value: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Value which indicates how to pronounce the value.</p>"""
    language: NotRequired["aws_sdk_geo_places.types.language_tag.LanguageTag"]
    r"""<p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    preferred: NotRequired[
        "aws_sdk_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Boolean which indicates if it the preferred pronunciation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeTranscription) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "language" in value:
        out["Language"] = value["language"]
    if "preferred" in value:
        out["Preferred"] = value["preferred"]
    return out


def deserialize_json(data: dict) -> PhonemeTranscription:
    out: PhonemeTranscription = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Language" in data:
        out["language"] = data["Language"]
    if "Preferred" in data:
        out["preferred"] = data["Preferred"]
    return out
