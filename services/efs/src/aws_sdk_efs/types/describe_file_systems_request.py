"""Generated from Smithy shape ``com.amazonaws.efs#DescribeFileSystemsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.creation_token
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.marker
    import aws_sdk_efs.types.max_items


class DescribeFileSystemsRequest(TypedDict):
    max_items: NotRequired["aws_sdk_efs.types.max_items.MaxItems"]
    """<p>(Optional) Specifies the maximum number of file systems to return in the response (integer). This number is automatically set to 100. The response is paginated at 100 per page if you have more than 100 file systems. </p>"""
    marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>(Optional) Opaque pagination token returned from a previous <code>DescribeFileSystems</code> operation (String). If present, specifies to continue the list from where the returning call had left off. </p>"""
    creation_token: NotRequired["aws_sdk_efs.types.creation_token.CreationToken"]
    """<p>(Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.</p>"""
    file_system_id: NotRequired["aws_sdk_efs.types.file_system_id.FileSystemId"]
    """<p>(Optional) ID of the file system whose description you want to retrieve (String).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFileSystemsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFileSystemsRequest:
    out: DescribeFileSystemsRequest = {}  # type: ignore[typeddict-item]
    return out
