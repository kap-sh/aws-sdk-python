"""Generated from Smithy shape ``com.amazonaws.backup#ListScanJobSummariesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.account_id
    import aws_sdk_backup.types.aggregation_period
    import aws_sdk_backup.types.malware_scanner
    import aws_sdk_backup.types.max_results
    import aws_sdk_backup.types.resource_type
    import aws_sdk_backup.types.scan_job_status
    import aws_sdk_backup.types.scan_result_status
    import aws_sdk_backup.types.string


class ListScanJobSummariesInput(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_backup.types.account_id.AccountId"]
    """<p>Returns the job count for the specified account.</p> <p>If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestor's account will be returned.</p> <p>Root, admin, and delegated administrator accounts can use the value <code>ANY</code> to return job counts from every account in the organization.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts from all accounts within the authenticated organization, then returns the sum.</p>"""
    resource_type: NotRequired["aws_sdk_backup.types.resource_type.ResourceType"]
    """<p>Returns the job count for the specified resource type. Use request <code>GetSupportedResourceTypes</code> to obtain strings for supported resource types.</p> <p>The the value <code>ANY</code> returns count of all resource types.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all resource types and returns the sum.</p>"""
    malware_scanner: NotRequired["aws_sdk_backup.types.malware_scanner.MalwareScanner"]
    """<p>Returns only the scan jobs for the specified malware scanner. Currently the only MalwareScanner is <code>GUARDDUTY</code>. But the field also supports <code>ANY</code>, and <code>AGGREGATE_ALL</code>.</p>"""
    scan_result_status: NotRequired[
        "aws_sdk_backup.types.scan_result_status.ScanResultStatus"
    ]
    """<p>Returns only the scan jobs for the specified scan results.</p>"""
    state: NotRequired["aws_sdk_backup.types.scan_job_status.ScanJobStatus"]
    """<p>Returns only the scan jobs for the specified scanning job state.</p>"""
    aggregation_period: NotRequired[
        "aws_sdk_backup.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code>The daily job count for the prior 1 day.</p> </li> <li> <p> <code>SEVEN_DAYS</code>The daily job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code>The daily job count for the prior 14 days.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p> <p>The value is an integer. Range of accepted values is from 1 to 500.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScanJobSummariesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScanJobSummariesInput:
    out: ListScanJobSummariesInput = {}  # type: ignore[typeddict-item]
    return out
