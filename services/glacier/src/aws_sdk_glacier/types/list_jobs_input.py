"""Generated from Smithy shape ``com.amazonaws.glacier#ListJobsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ListJobsInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    limit: NotRequired["int"]
    """<p>The maximum number of jobs to be returned. The default limit is 50. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.</p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.</p>"""
    statuscode: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The type of job status to return. You can specify the following values: <code>InProgress</code>, <code>Succeeded</code>, or <code>Failed</code>.</p>"""
    completed: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The state of the jobs to return. You can specify <code>true</code> or <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobsInput:
    out: ListJobsInput = {}  # type: ignore[typeddict-item]
    return out
