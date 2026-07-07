"""Generated from Smithy shape ``com.amazonaws.pinpoint#WriteSegmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.segment_dimensions
    import aws_sdk_pinpoint.types.segment_group_list


class WriteSegmentRequest(TypedDict, closed=True):
    dimensions: NotRequired[
        "aws_sdk_pinpoint.types.segment_dimensions.SegmentDimensions"
    ]
    """<p>The criteria that define the dimensions for the segment.</p>"""
    name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the segment.</p>"""
    segment_groups: NotRequired[
        "aws_sdk_pinpoint.types.segment_group_list.SegmentGroupList"
    ]
    """<p>The segment group to use and the dimensions to apply to the group's base segments in order to build the segment. A segment group can consist of zero or more base segments. Your request can include only one segment group.</p>"""
    tags: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    r"""<note><p>As of <b>22-05-2023</b> tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html\">Tags</a> in the <i>API Reference for Amazon Pinpoint</i>, <a href=\"https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html\">resourcegroupstaggingapi</a> commands in the <i>AWS Command Line Interface Documentation</i> or <a href=\"https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html\">resourcegroupstaggingapi</a> in the <i>AWS SDK</i>.</p></note> <p>(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the segment. Each tag consists of a required tag key and an associated tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteSegmentRequest) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_pinpoint.types.segment_dimensions

        out["Dimensions"] = aws_sdk_pinpoint.types.segment_dimensions.serialize_json(
            value["dimensions"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "segment_groups" in value:
        import aws_sdk_pinpoint.types.segment_group_list

        out["SegmentGroups"] = aws_sdk_pinpoint.types.segment_group_list.serialize_json(
            value["segment_groups"]
        )
    if "tags" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> WriteSegmentRequest:
    out: WriteSegmentRequest = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_pinpoint.types.segment_dimensions

        out["dimensions"] = aws_sdk_pinpoint.types.segment_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "SegmentGroups" in data:
        import aws_sdk_pinpoint.types.segment_group_list

        out["segment_groups"] = (
            aws_sdk_pinpoint.types.segment_group_list.deserialize_json(
                data["SegmentGroups"]
            )
        )
    if "tags" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["tags"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["tags"]
        )
    return out
