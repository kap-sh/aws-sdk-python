"""Generated from Smithy shape ``com.amazonaws.backup#ListIndexedRecoveryPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.index_status
    import aws_sdk_backup.types.max_results
    import aws_sdk_backup.types.resource_type
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class ListIndexedRecoveryPointsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned recovery points.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of indexed recovery points, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["aws_sdk_backup.types.max_results.MaxResults"]
    """<p>The maximum number of resource list items to be returned.</p>"""
    source_resource_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.</p>"""
    created_before: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>Returns only indexed recovery points that were created before the specified date.</p>"""
    created_after: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>Returns only indexed recovery points that were created after the specified date.</p>"""
    resource_type: NotRequired["aws_sdk_backup.types.resource_type.ResourceType"]
    """<p>Returns a list of indexed recovery points for the specified resource type(s).</p> <p>Accepted values include:</p> <ul> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul>"""
    index_status: NotRequired["aws_sdk_backup.types.index_status.IndexStatus"]
    """<p>Include this parameter to filter the returned list by the indicated statuses.</p> <p>Accepted values: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexedRecoveryPointsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIndexedRecoveryPointsInput:
    out: ListIndexedRecoveryPointsInput = {}  # type: ignore[typeddict-item]
    return out
