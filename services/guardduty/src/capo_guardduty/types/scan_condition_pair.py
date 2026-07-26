"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanConditionPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.tag_key
    import capo_guardduty.types.tag_value


class ScanConditionPair(TypedDict, closed=True):
    key: NotRequired["capo_guardduty.types.tag_key.TagKey"]
    """<p>Represents the <b>key</b> in the map condition.</p>"""
    value: NotRequired["capo_guardduty.types.tag_value.TagValue"]
    """<p>Represents optional <b>value</b> in the map condition. If not specified, only the <b>key</b> will be matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanConditionPair) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ScanConditionPair:
    out: ScanConditionPair = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
