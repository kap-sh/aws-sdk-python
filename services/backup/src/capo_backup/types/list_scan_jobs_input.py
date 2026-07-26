"""Generated from Smithy shape ``com.amazonaws.backup#ListScanJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backup.types.list_scan_jobs_input_max_results_integer
    import capo_backup.types.malware_scanner
    import capo_backup.types.scan_resource_type
    import capo_backup.types.scan_result_status
    import capo_backup.types.scan_state


class ListScanJobsInput(TypedDict, closed=True):
    by_account_id: NotRequired["str"]
    """<p>The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.</p> <p>If used from an Amazon Web Services Organizations management account, passing <code>*</code> returns all jobs across the organization.</p> <p>Pattern: <code>^[0-9]{12}$</code> </p>"""
    by_backup_vault_name: NotRequired["str"]
    r"""<p>Returns only scan jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <p>Pattern: <code>^[a-zA-Z0-9\-\_\.]{2,50}$</code> </p>"""
    by_complete_after: NotRequired["datetime.datetime"]
    """<p>Returns only scan jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_complete_before: NotRequired["datetime.datetime"]
    """<p>Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>"""
    by_malware_scanner: NotRequired["capo_backup.types.malware_scanner.MalwareScanner"]
    """<p>Returns only the scan jobs for the specified malware scanner. Currently only supports <code>GUARDDUTY</code>.</p>"""
    by_recovery_point_arn: NotRequired["str"]
    """<p>Returns only the scan jobs that are ran against the specified recovery point.</p>"""
    by_resource_arn: NotRequired["str"]
    """<p>Returns only scan jobs that match the specified resource Amazon Resource Name (ARN).</p>"""
    by_resource_type: NotRequired[
        "capo_backup.types.scan_resource_type.ScanResourceType"
    ]
    r"""<p>Returns restore testing selections by the specified restore testing plan name.</p> <ul> <li> <p> <code>EBS</code>for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code>for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>S3</code>for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul> <p>Pattern: <code>^[a-zA-Z0-9\-\_\.]{1,50}$</code> </p>"""
    by_scan_result_status: NotRequired[
        "capo_backup.types.scan_result_status.ScanResultStatus"
    ]
    """<p>Returns only the scan jobs for the specified scan results:</p> <ul> <li> <p> <code>THREATS_FOUND</code> </p> </li> <li> <p> <code>NO_THREATS_FOUND</code> </p> </li> </ul>"""
    by_state: NotRequired["capo_backup.types.scan_state.ScanState"]
    """<p>Returns only the scan jobs for the specified scanning job state.</p>"""
    max_results: NotRequired[
        "capo_backup.types.list_scan_jobs_input_max_results_integer.ListScanJobsInputMaxResultsInteger"
    ]
    """<p>The maximum number of items to be returned.</p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScanJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScanJobsInput:
    out: ListScanJobsInput = {}  # type: ignore[typeddict-item]
    return out
