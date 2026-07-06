"""Generated from Smithy shape ``com.amazonaws.iot#DescribeJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.job
    import aws_sdk_iot.types.job_document_source


class DescribeJobResponse(TypedDict, closed=True):
    document_source: NotRequired[
        "aws_sdk_iot.types.job_document_source.JobDocumentSource"
    ]
    """<p>An S3 link to the job document.</p>"""
    job: NotRequired["aws_sdk_iot.types.job.Job"]
    """<p>Information about the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobResponse) -> dict:
    out: dict = {}
    if "document_source" in value:
        out["documentSource"] = value["document_source"]
    if "job" in value:
        import aws_sdk_iot.types.job

        out["job"] = aws_sdk_iot.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> DescribeJobResponse:
    out: DescribeJobResponse = {}  # type: ignore[typeddict-item]
    if "documentSource" in data:
        out["document_source"] = data["documentSource"]
    if "job" in data:
        import aws_sdk_iot.types.job

        out["job"] = aws_sdk_iot.types.job.deserialize_json(data["job"])
    return out
