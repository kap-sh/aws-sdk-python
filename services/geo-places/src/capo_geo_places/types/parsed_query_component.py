"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQueryComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class ParsedQueryComponent(TypedDict, closed=True):
    start_index: NotRequired["int"]
    """<p>Start index of the parsed query component.</p>"""
    end_index: NotRequired["int"]
    """<p>End index of the parsed query component.</p>"""
    value: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Value of the parsed query component.</p>"""
    query_component: NotRequired[
        "capo_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>The address component that the parsed query component corresponds to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQueryComponent) -> dict:
    out: dict = {}
    if "start_index" in value:
        out["StartIndex"] = value["start_index"]
    if "end_index" in value:
        out["EndIndex"] = value["end_index"]
    if "value" in value:
        out["Value"] = value["value"]
    if "query_component" in value:
        out["QueryComponent"] = value["query_component"]
    return out


def deserialize_json(data: dict) -> ParsedQueryComponent:
    out: ParsedQueryComponent = {}  # type: ignore[typeddict-item]
    if "StartIndex" in data:
        out["start_index"] = data["StartIndex"]
    if "EndIndex" in data:
        out["end_index"] = data["EndIndex"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "QueryComponent" in data:
        out["query_component"] = data["QueryComponent"]
    return out
