"""Generated from Smithy shape ``com.amazonaws.georoutes#LocalizedString``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.language_tag
    import aws_sdk_geo_routes.types.sensitive_string


class LocalizedString(TypedDict, closed=True):
    language: NotRequired["aws_sdk_geo_routes.types.language_tag.LanguageTag"]
    """<p>A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language can't be provided.</p>"""
    value: "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    """<p>The value of the localized string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalizedString) -> dict:
    out: dict = {}
    if "language" in value:
        out["Language"] = value["language"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> LocalizedString:
    out: LocalizedString = {}  # type: ignore[typeddict-item]
    if "Language" in data:
        out["language"] = data["Language"]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("LocalizedString.value required")
    return out
