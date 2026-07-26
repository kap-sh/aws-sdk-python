"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class SourceSegment(TypedDict, closed=True):
    segment_definition_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the segment definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceSegment) -> dict:
    out: dict = {}
    if "segment_definition_name" in value:
        out["SegmentDefinitionName"] = value["segment_definition_name"]
    return out


def deserialize_json(data: dict) -> SourceSegment:
    out: SourceSegment = {}  # type: ignore[typeddict-item]
    if "SegmentDefinitionName" in data:
        out["segment_definition_name"] = data["SegmentDefinitionName"]
    return out
