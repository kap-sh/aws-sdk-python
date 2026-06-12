"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class SourceSegment(TypedDict):
    segment_definition_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
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
