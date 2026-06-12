"""Generated from Smithy shape ``com.amazonaws.sesv2#FailureInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.error_message
    import aws_sdk_sesv2.types.failed_records_s3_url


class FailureInfo(TypedDict):
    failed_records_s3_url: NotRequired[
        "aws_sdk_sesv2.types.failed_records_s3_url.FailedRecordsS3Url"
    ]
    """<p>An Amazon S3 pre-signed URL that contains all the failed records and related information.</p>"""
    error_message: NotRequired["aws_sdk_sesv2.types.error_message.ErrorMessage"]
    """<p>A message about why the job failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureInfo) -> dict:
    out: dict = {}
    if "failed_records_s3_url" in value:
        out["FailedRecordsS3Url"] = value["failed_records_s3_url"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailureInfo:
    out: FailureInfo = {}  # type: ignore[typeddict-item]
    if "FailedRecordsS3Url" in data:
        out["failed_records_s3_url"] = data["FailedRecordsS3Url"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
