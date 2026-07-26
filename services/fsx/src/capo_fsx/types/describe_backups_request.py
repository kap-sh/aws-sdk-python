"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeBackupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.backup_ids
    import capo_fsx.types.filters
    import capo_fsx.types.max_results
    import capo_fsx.types.next_token


class DescribeBackupsRequest(TypedDict, closed=True):
    backup_ids: NotRequired["capo_fsx.types.backup_ids.BackupIds"]
    """<p>The IDs of the backups that you want to retrieve. This parameter value overrides any filters. If any IDs aren't found, a <code>BackupNotFound</code> error occurs.</p>"""
    filters: NotRequired["capo_fsx.types.filters.Filters"]
    """<p>The filters structure. The supported names are <code>file-system-id</code>, <code>backup-type</code>, <code>file-system-type</code>, and <code>volume-id</code>.</p>"""
    max_results: NotRequired["capo_fsx.types.max_results.MaxResults"]
    """<p>Maximum number of backups to return in the response. This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]
    """<p>An opaque pagination token returned from a previous <code>DescribeBackups</code> operation. If a token is present, the operation continues the list from where the returning call left off.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBackupsRequest) -> dict:
    out: dict = {}
    if "backup_ids" in value:
        import capo_fsx.types.backup_ids

        out["BackupIds"] = capo_fsx.types.backup_ids.serialize_aws_json_1_1(
            value["backup_ids"]
        )
    if "filters" in value:
        import capo_fsx.types.filters

        out["Filters"] = capo_fsx.types.filters.serialize_aws_json_1_1(value["filters"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBackupsRequest:
    out: DescribeBackupsRequest = {}  # type: ignore[typeddict-item]
    if "BackupIds" in data:
        import capo_fsx.types.backup_ids

        out["backup_ids"] = capo_fsx.types.backup_ids.deserialize_aws_json_1_1(
            data["BackupIds"]
        )
    if "Filters" in data:
        import capo_fsx.types.filters

        out["filters"] = capo_fsx.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
