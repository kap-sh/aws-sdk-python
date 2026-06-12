"""Generated from Smithy shape ``com.amazonaws.efs#DescribeReplicationConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.max_results
    import aws_sdk_efs.types.token


class DescribeReplicationConfigurationsRequest(TypedDict):
    file_system_id: NotRequired["aws_sdk_efs.types.file_system_id.FileSystemId"]
    """<p>You can retrieve the replication configuration for a specific file system by providing its file system ID. For cross-account,cross-region replication, an account can only describe the replication configuration for a file system in its own Region.</p>"""
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p> <code>NextToken</code> is present if the response is paginated. You can use <code>NextToken</code> in a subsequent request to fetch the next page of output.</p>"""
    max_results: NotRequired["aws_sdk_efs.types.max_results.MaxResults"]
    """<p>(Optional) To limit the number of objects returned in a response, you can specify the <code>MaxItems</code> parameter. The default value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationsRequest:
    out: DescribeReplicationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
