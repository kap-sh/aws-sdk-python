"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.arn
    import capo_backup.types.max_results
    import capo_backup.types.resource_type
    import capo_backup.types.restore_job_status
    import capo_backup.types.string
    import capo_backup.types.timestamp


class ListRestoreJobsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""
    by_account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID.</p>"""
    by_resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>Include this parameter to return only restore jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>"""
    by_created_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only restore jobs that were created before the specified date.</p>"""
    by_created_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only restore jobs that were created after the specified date.</p>"""
    by_status: NotRequired["capo_backup.types.restore_job_status.RestoreJobStatus"]
    """<p>Returns only restore jobs associated with the specified job status.</p>"""
    by_complete_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_complete_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_restore_testing_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>This returns only restore testing jobs that match the specified resource Amazon Resource Name (ARN).</p>"""
    by_parent_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>This is a filter to list child (nested) restore jobs based on parent restore job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRestoreJobsInput:
    out: ListRestoreJobsInput = {}  # type: ignore[typeddict-item]
    return out
