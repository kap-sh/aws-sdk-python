"""Generated from Smithy shape ``com.amazonaws.efs#DescribeAccessPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.access_point_id
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.max_results
    import aws_sdk_efs.types.token


class DescribeAccessPointsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_efs.types.max_results.MaxResults"]
    """<p>(Optional) When retrieving all access points for a file system, you can optionally specify the <code>MaxItems</code> parameter to limit the number of objects returned in a response. The default value is 100. </p>"""
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p> <code>NextToken</code> is present if the response is paginated. You can use <code>NextMarker</code> in the subsequent request to fetch the next page of access point descriptions.</p>"""
    access_point_id: NotRequired["aws_sdk_efs.types.access_point_id.AccessPointId"]
    """<p>(Optional) Specifies an EFS access point to describe in the response; mutually exclusive with <code>FileSystemId</code>.</p>"""
    file_system_id: NotRequired["aws_sdk_efs.types.file_system_id.FileSystemId"]
    """<p>(Optional) If you provide a <code>FileSystemId</code>, EFS returns all access points for that file system; mutually exclusive with <code>AccessPointId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessPointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccessPointsRequest:
    out: DescribeAccessPointsRequest = {}  # type: ignore[typeddict-item]
    return out
