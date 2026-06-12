"""Generated from Smithy shape ``com.amazonaws.geoplaces#Highlight``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.sensitive_string


class Highlight(TypedDict):
    start_index: NotRequired["int"]
    """<p>Start index of the highlight.</p>"""
    end_index: NotRequired["int"]
    """<p>End index of the highlight.</p>"""
    value: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The highlight's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Highlight) -> dict:
    out: dict = {}
    if "start_index" in value:
        out["StartIndex"] = value["start_index"]
    if "end_index" in value:
        out["EndIndex"] = value["end_index"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Highlight:
    out: Highlight = {}  # type: ignore[typeddict-item]
    if "StartIndex" in data:
        out["start_index"] = data["StartIndex"]
    if "EndIndex" in data:
        out["end_index"] = data["EndIndex"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
