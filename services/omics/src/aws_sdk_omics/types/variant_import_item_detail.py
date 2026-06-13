"""Generated from Smithy shape ``com.amazonaws.omics#VariantImportItemDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.job_status
    import aws_sdk_omics.types.job_status_msg
    import aws_sdk_omics.types.s3_uri


class VariantImportItemDetail(TypedDict):
    source: "aws_sdk_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""
    job_status: "aws_sdk_omics.types.job_status.JobStatus"
    """<p>The item's job status.</p>"""
    status_message: NotRequired["aws_sdk_omics.types.job_status_msg.JobStatusMsg"]
    """<p> A message that provides additional context about a job </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantImportItemDetail) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["jobStatus"] = value["job_status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> VariantImportItemDetail:
    out: VariantImportItemDetail = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("VariantImportItemDetail.source required")
    if "jobStatus" in data:
        out["job_status"] = data["jobStatus"]
    else:
        raise DeserializationError("VariantImportItemDetail.job_status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
