"""Generated from Smithy shape ``com.amazonaws.sesv2#ListExportJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.export_source_type
    import aws_sdk_sesv2.types.job_status
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token


class ListExportJobsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>The pagination token returned from a previous call to <code>ListExportJobs</code> to indicate the position in the list of export jobs.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>Maximum number of export jobs to return at once. Use this parameter to paginate results. If additional export jobs exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent calls to <code>ListExportJobs</code> to retrieve additional export jobs.</p>"""
    export_source_type: NotRequired[
        "aws_sdk_sesv2.types.export_source_type.ExportSourceType"
    ]
    """<p>A value used to list export jobs that have a certain <code>ExportSourceType</code>.</p>"""
    job_status: NotRequired["aws_sdk_sesv2.types.job_status.JobStatus"]
    """<p>A value used to list export jobs that have a certain <code>JobStatus</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "export_source_type" in value:
        import aws_sdk_sesv2.types.export_source_type

        out["ExportSourceType"] = aws_sdk_sesv2.types.export_source_type.serialize_json(
            value["export_source_type"]
        )
    if "job_status" in value:
        import aws_sdk_sesv2.types.job_status

        out["JobStatus"] = aws_sdk_sesv2.types.job_status.serialize_json(
            value["job_status"]
        )
    return out


def deserialize_json(data: dict) -> ListExportJobsRequest:
    out: ListExportJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "ExportSourceType" in data:
        import aws_sdk_sesv2.types.export_source_type

        out["export_source_type"] = (
            aws_sdk_sesv2.types.export_source_type.deserialize_json(
                data["ExportSourceType"]
            )
        )
    if "JobStatus" in data:
        import aws_sdk_sesv2.types.job_status

        out["job_status"] = aws_sdk_sesv2.types.job_status.deserialize_json(
            data["JobStatus"]
        )
    return out
