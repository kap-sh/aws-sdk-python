"""Generated from Smithy shape ``com.amazonaws.wisdom#ListImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.import_job_list
    import aws_sdk_wisdom.types.non_empty_string


class ListImportJobsResponse(TypedDict, closed=True):
    import_job_summaries: "aws_sdk_wisdom.types.import_job_list.ImportJobList"
    """<p>Summary information about the import jobs.</p>"""
    next_token: NotRequired["aws_sdk_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.import_job_list

    out["importJobSummaries"] = aws_sdk_wisdom.types.import_job_list.serialize_json(
        value["import_job_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportJobsResponse:
    out: ListImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "importJobSummaries" in data:
        import aws_sdk_wisdom.types.import_job_list

        out["import_job_summaries"] = (
            aws_sdk_wisdom.types.import_job_list.deserialize_json(
                data["importJobSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListImportJobsResponse.import_job_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
