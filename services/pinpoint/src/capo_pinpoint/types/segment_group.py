"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.list_of_segment_dimensions
    import capo_pinpoint.types.list_of_segment_reference
    import capo_pinpoint.types.source_type
    import capo_pinpoint.types.type


class SegmentGroup(TypedDict, closed=True):
    dimensions: NotRequired[
        "capo_pinpoint.types.list_of_segment_dimensions.ListOfSegmentDimensions"
    ]
    """<p>An array that defines the dimensions for the segment.</p>"""
    source_segments: NotRequired[
        "capo_pinpoint.types.list_of_segment_reference.ListOfSegmentReference"
    ]
    """<p>The base segment to build the segment on. A base segment, also referred to as a <i>source segment</i>, defines the initial population of endpoints for a segment. When you add dimensions to a segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.</p> <p>You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the Amazon Pinpoint console displays a segment size estimate that indicates the size of the imported segment without any filters applied to it.</p>"""
    source_type: NotRequired["capo_pinpoint.types.source_type.SourceType"]
    """<p>Specifies how to handle multiple base segments for the segment. For example, if you specify three base segments for the segment, whether the resulting segment is based on all, any, or none of the base segments.</p>"""
    type: NotRequired["capo_pinpoint.types.type.Type"]
    """<p>Specifies how to handle multiple dimensions for the segment. For example, if you specify three dimensions for the segment, whether the resulting segment includes endpoints that match all, any, or none of the dimensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentGroup) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_pinpoint.types.list_of_segment_dimensions

        out["Dimensions"] = (
            capo_pinpoint.types.list_of_segment_dimensions.serialize_json(
                value["dimensions"]
            )
        )
    if "source_segments" in value:
        import capo_pinpoint.types.list_of_segment_reference

        out["SourceSegments"] = (
            capo_pinpoint.types.list_of_segment_reference.serialize_json(
                value["source_segments"]
            )
        )
    if "source_type" in value:
        import capo_pinpoint.types.source_type

        out["SourceType"] = capo_pinpoint.types.source_type.serialize_json(
            value["source_type"]
        )
    if "type" in value:
        import capo_pinpoint.types.type

        out["Type"] = capo_pinpoint.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SegmentGroup:
    out: SegmentGroup = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_pinpoint.types.list_of_segment_dimensions

        out["dimensions"] = (
            capo_pinpoint.types.list_of_segment_dimensions.deserialize_json(
                data["Dimensions"]
            )
        )
    if "SourceSegments" in data:
        import capo_pinpoint.types.list_of_segment_reference

        out["source_segments"] = (
            capo_pinpoint.types.list_of_segment_reference.deserialize_json(
                data["SourceSegments"]
            )
        )
    if "SourceType" in data:
        import capo_pinpoint.types.source_type

        out["source_type"] = capo_pinpoint.types.source_type.deserialize_json(
            data["SourceType"]
        )
    if "Type" in data:
        import capo_pinpoint.types.type

        out["type"] = capo_pinpoint.types.type.deserialize_json(data["Type"])
    return out
