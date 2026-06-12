"""Generated from Smithy shape ``com.amazonaws.efs#DescribeTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.marker
    import aws_sdk_efs.types.max_items


class DescribeTagsRequest(TypedDict):
    max_items: NotRequired["aws_sdk_efs.types.max_items.MaxItems"]
    """<p>(Optional) The maximum number of file system tags to return in the response. Currently, this number is automatically set to 100, and other values are ignored. The response is paginated at 100 per page if you have more than 100 tags.</p>"""
    marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>(Optional) An opaque pagination token returned from a previous <code>DescribeTags</code> operation (String). If present, it specifies to continue the list from where the previous call left off.</p>"""
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose tag set you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTagsRequest:
    out: DescribeTagsRequest = {}  # type: ignore[typeddict-item]
    return out
