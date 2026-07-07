"""Generated from Smithy shape ``com.amazonaws.backupsearch#StartSearchJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backupsearch.types.generic_id
    import aws_sdk_backupsearch.types.search_job_arn


class StartSearchJobOutput(TypedDict, closed=True):
    search_job_arn: NotRequired[
        "aws_sdk_backupsearch.types.search_job_arn.SearchJobArn"
    ]
    """<p>The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The date and time that a job was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    search_job_identifier: NotRequired[
        "aws_sdk_backupsearch.types.generic_id.GenericId"
    ]
    """<p>The unique string that specifies the search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSearchJobOutput) -> dict:
    out: dict = {}
    if "search_job_arn" in value:
        out["SearchJobArn"] = value["search_job_arn"]
    if "creation_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CreationTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "search_job_identifier" in value:
        out["SearchJobIdentifier"] = value["search_job_identifier"]
    return out


def deserialize_json(data: dict) -> StartSearchJobOutput:
    out: StartSearchJobOutput = {}  # type: ignore[typeddict-item]
    if "SearchJobArn" in data:
        out["search_job_arn"] = data["SearchJobArn"]
    if "CreationTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "SearchJobIdentifier" in data:
        out["search_job_identifier"] = data["SearchJobIdentifier"]
    return out
