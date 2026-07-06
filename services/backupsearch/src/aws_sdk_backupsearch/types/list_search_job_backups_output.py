"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchJobBackupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.search_job_backups_results


class ListSearchJobBackupsOutput(TypedDict, closed=True):
    results: (
        "aws_sdk_backupsearch.types.search_job_backups_results.SearchJobBackupsResults"
    )
    """<p>The recovery points returned the results of a search job</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchJobBackupsOutput) -> dict:
    out: dict = {}
    import aws_sdk_backupsearch.types.search_job_backups_results

    out["Results"] = (
        aws_sdk_backupsearch.types.search_job_backups_results.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSearchJobBackupsOutput:
    out: ListSearchJobBackupsOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_backupsearch.types.search_job_backups_results

        out["results"] = (
            aws_sdk_backupsearch.types.search_job_backups_results.deserialize_json(
                data["Results"]
            )
        )
    else:
        raise DeserializationError("ListSearchJobBackupsOutput.results required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
