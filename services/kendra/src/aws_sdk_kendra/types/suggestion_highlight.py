"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionHighlight``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.integer


class SuggestionHighlight(TypedDict):
    begin_offset: NotRequired["aws_sdk_kendra.types.integer.Integer"]
    """<p>The zero-based location in the response string where the highlight starts.</p>"""
    end_offset: NotRequired["aws_sdk_kendra.types.integer.Integer"]
    """<p>The zero-based location in the response string where the highlight ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionHighlight) -> dict:
    out: dict = {}
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SuggestionHighlight:
    out: SuggestionHighlight = {}  # type: ignore[typeddict-item]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    return out
