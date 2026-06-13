"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backupsearch.types.generic_id
    import aws_sdk_backupsearch.types.search_job_arn
    import aws_sdk_backupsearch.types.search_job_state
    import aws_sdk_backupsearch.types.search_scope_summary


class SearchJobSummary(TypedDict):
    search_job_identifier: NotRequired[
        "aws_sdk_backupsearch.types.generic_id.GenericId"
    ]
    """<p>The unique string that specifies the search job.</p>"""
    search_job_arn: NotRequired[
        "aws_sdk_backupsearch.types.search_job_arn.SearchJobArn"
    ]
    """<p>The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.</p>"""
    name: NotRequired["str"]
    """<p>This is the name of the search job.</p>"""
    status: NotRequired["aws_sdk_backupsearch.types.search_job_state.SearchJobState"]
    """<p>This is the status of the search job.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>This is the creation time of the search job.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>This is the completion time of the search job.</p>"""
    search_scope_summary: NotRequired[
        "aws_sdk_backupsearch.types.search_scope_summary.SearchScopeSummary"
    ]
    """<p>Returned summary of the specified search job scope, including: </p> <ul> <li> <p>TotalBackupsToScanCount, the number of recovery points returned by the search.</p> </li> <li> <p>TotalItemsToScanCount, the number of items returned by the search.</p> </li> </ul>"""
    status_message: NotRequired["str"]
    """<p>A status message will be returned for either a earch job with a status of <code>ERRORED</code> or a status of <code>COMPLETED</code> jobs with issues.</p> <p>For example, a message may say that a search contained recovery points unable to be scanned because of a permissions issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobSummary) -> dict:
    out: dict = {}
    if "search_job_identifier" in value:
        out["SearchJobIdentifier"] = value["search_job_identifier"]
    if "search_job_arn" in value:
        out["SearchJobArn"] = value["search_job_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_backupsearch.types.search_job_state

        out["Status"] = aws_sdk_backupsearch.types.search_job_state.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CreationTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "completion_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CompletionTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["completion_time"]
            )
        )
    if "search_scope_summary" in value:
        import aws_sdk_backupsearch.types.search_scope_summary

        out["SearchScopeSummary"] = (
            aws_sdk_backupsearch.types.search_scope_summary.serialize_json(
                value["search_scope_summary"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> SearchJobSummary:
    out: SearchJobSummary = {}  # type: ignore[typeddict-item]
    if "SearchJobIdentifier" in data:
        out["search_job_identifier"] = data["SearchJobIdentifier"]
    if "SearchJobArn" in data:
        out["search_job_arn"] = data["SearchJobArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_backupsearch.types.search_job_state

        out["status"] = aws_sdk_backupsearch.types.search_job_state.deserialize_json(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CompletionTime"]
            )
        )
    if "SearchScopeSummary" in data:
        import aws_sdk_backupsearch.types.search_scope_summary

        out["search_scope_summary"] = (
            aws_sdk_backupsearch.types.search_scope_summary.deserialize_json(
                data["SearchScopeSummary"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
