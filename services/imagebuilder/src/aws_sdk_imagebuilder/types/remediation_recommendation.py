"""Generated from Smithy shape ``com.amazonaws.imagebuilder#RemediationRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string


class RemediationRecommendation(TypedDict, closed=True):
    text: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The recommended course of action to remediate the finding.</p>"""
    url: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>A link to more information about the recommended remediation for this vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationRecommendation) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RemediationRecommendation:
    out: RemediationRecommendation = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "url" in data:
        out["url"] = data["url"]
    return out
