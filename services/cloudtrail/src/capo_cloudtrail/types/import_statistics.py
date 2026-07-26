"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.long


class ImportStatistics(TypedDict, closed=True):
    prefixes_found: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p> The number of S3 prefixes found for the import. </p>"""
    prefixes_completed: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p> The number of S3 prefixes that completed import. </p>"""
    files_completed: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p>The number of log files that completed import.</p>"""
    events_completed: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p> The number of trail events imported into the event data store. </p>"""
    failed_entries: NotRequired["capo_cloudtrail.types.long.Long"]
    """<p> The number of failed entries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportStatistics) -> dict:
    out: dict = {}
    if "prefixes_found" in value:
        out["PrefixesFound"] = value["prefixes_found"]
    if "prefixes_completed" in value:
        out["PrefixesCompleted"] = value["prefixes_completed"]
    if "files_completed" in value:
        out["FilesCompleted"] = value["files_completed"]
    if "events_completed" in value:
        out["EventsCompleted"] = value["events_completed"]
    if "failed_entries" in value:
        out["FailedEntries"] = value["failed_entries"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportStatistics:
    out: ImportStatistics = {}  # type: ignore[typeddict-item]
    if "PrefixesFound" in data:
        out["prefixes_found"] = data["PrefixesFound"]
    if "PrefixesCompleted" in data:
        out["prefixes_completed"] = data["PrefixesCompleted"]
    if "FilesCompleted" in data:
        out["files_completed"] = data["FilesCompleted"]
    if "EventsCompleted" in data:
        out["events_completed"] = data["EventsCompleted"]
    if "FailedEntries" in data:
        out["failed_entries"] = data["FailedEntries"]
    return out
