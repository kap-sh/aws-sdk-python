"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesTagCriterionPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class SearchResourcesTagCriterionPair(TypedDict, closed=True):
    key: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The value for the tag key to use in the condition.</p>"""
    value: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The tag value to use in the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesTagCriterionPair) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SearchResourcesTagCriterionPair:
    out: SearchResourcesTagCriterionPair = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
