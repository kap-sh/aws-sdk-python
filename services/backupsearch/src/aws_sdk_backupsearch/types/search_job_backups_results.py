"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchJobBackupsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.search_job_backups_result

SearchJobBackupsResults: TypeAlias = list[
    "aws_sdk_backupsearch.types.search_job_backups_result.SearchJobBackupsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobBackupsResults) -> list:
    import aws_sdk_backupsearch.types.search_job_backups_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backupsearch.types.search_job_backups_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchJobBackupsResults:
    import aws_sdk_backupsearch.types.search_job_backups_result

    out: SearchJobBackupsResults = []
    for item in data:
        out.append(
            aws_sdk_backupsearch.types.search_job_backups_result.deserialize_json(item)
        )
    return out
