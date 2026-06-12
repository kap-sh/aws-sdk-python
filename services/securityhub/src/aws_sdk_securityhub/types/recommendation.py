"""Generated from Smithy shape ``com.amazonaws.securityhub#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class Recommendation(TypedDict):
    text: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Describes the recommended steps to take to remediate an issue identified in a finding.</p> <p>Length Constraints: Minimum of 1 length. Maximum of 512 length.</p>"""
    url: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A URL to a page or site that contains information about how to remediate a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
