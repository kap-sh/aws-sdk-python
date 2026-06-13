"""Generated from Smithy shape ``com.amazonaws.inspector2#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.non_empty_string


class Recommendation(TypedDict):
    text: NotRequired["aws_sdk_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The recommended course of action to remediate the finding.</p>"""
    url: NotRequired["aws_sdk_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The URL address to the CVE remediation recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
