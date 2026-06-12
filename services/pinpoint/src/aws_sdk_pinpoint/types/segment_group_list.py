"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentGroupList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.include
    import aws_sdk_pinpoint.types.list_of_segment_group


class SegmentGroupList(TypedDict):
    groups: NotRequired[
        "aws_sdk_pinpoint.types.list_of_segment_group.ListOfSegmentGroup"
    ]
    """<p>An array that defines the set of segment criteria to evaluate when handling segment groups for the segment.</p>"""
    include: NotRequired["aws_sdk_pinpoint.types.include.Include"]
    """<p>Specifies how to handle multiple segment groups for the segment. For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentGroupList) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_pinpoint.types.list_of_segment_group

        out["Groups"] = aws_sdk_pinpoint.types.list_of_segment_group.serialize_json(
            value["groups"]
        )
    if "include" in value:
        import aws_sdk_pinpoint.types.include

        out["Include"] = aws_sdk_pinpoint.types.include.serialize_json(value["include"])
    return out


def deserialize_json(data: dict) -> SegmentGroupList:
    out: SegmentGroupList = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_pinpoint.types.list_of_segment_group

        out["groups"] = aws_sdk_pinpoint.types.list_of_segment_group.deserialize_json(
            data["Groups"]
        )
    if "Include" in data:
        import aws_sdk_pinpoint.types.include

        out["include"] = aws_sdk_pinpoint.types.include.deserialize_json(
            data["Include"]
        )
    return out
