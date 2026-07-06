"""Generated from Smithy shape ``com.amazonaws.omics#ListReadSetExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.export_read_set_job_detail_list
    import aws_sdk_omics.types.next_token


class ListReadSetExportJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    export_jobs: NotRequired[
        "aws_sdk_omics.types.export_read_set_job_detail_list.ExportReadSetJobDetailList"
    ]
    """<p>A list of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadSetExportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "export_jobs" in value:
        import aws_sdk_omics.types.export_read_set_job_detail_list

        out["exportJobs"] = (
            aws_sdk_omics.types.export_read_set_job_detail_list.serialize_json(
                value["export_jobs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReadSetExportJobsResponse:
    out: ListReadSetExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "exportJobs" in data:
        import aws_sdk_omics.types.export_read_set_job_detail_list

        out["export_jobs"] = (
            aws_sdk_omics.types.export_read_set_job_detail_list.deserialize_json(
                data["exportJobs"]
            )
        )
    return out
