"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UploadJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.expiration_days_integer
    import aws_sdk_customer_profiles.types.status_reason
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.upload_job_status
    import aws_sdk_customer_profiles.types.uuid


class UploadJobItem(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of the upload job. </p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The name of the upload job. </p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.upload_job_status.UploadJobStatus"
    ]
    """<p>The current status of the upload job. </p>"""
    status_reason: NotRequired[
        "aws_sdk_customer_profiles.types.status_reason.StatusReason"
    ]
    """<p>The reason for the current status of the upload job. </p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the upload job was created. </p>"""
    completed_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the upload job was completed. </p>"""
    data_expiry: NotRequired[
        "aws_sdk_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
    ]
    """<p>The expiry duration for the profiles ingested with the upload job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadJobItem) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_customer_profiles.types.upload_job_status

        out["Status"] = (
            aws_sdk_customer_profiles.types.upload_job_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_customer_profiles.types.status_reason

        out["StatusReason"] = (
            aws_sdk_customer_profiles.types.status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "completed_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["CompletedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["completed_at"]
        )
    if "data_expiry" in value:
        out["DataExpiry"] = value["data_expiry"]
    return out


def deserialize_json(data: dict) -> UploadJobItem:
    out: UploadJobItem = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Status" in data:
        import aws_sdk_customer_profiles.types.upload_job_status

        out["status"] = (
            aws_sdk_customer_profiles.types.upload_job_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_customer_profiles.types.status_reason

        out["status_reason"] = (
            aws_sdk_customer_profiles.types.status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "CompletedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["completed_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["CompletedAt"]
            )
        )
    if "DataExpiry" in data:
        out["data_expiry"] = data["DataExpiry"]
    return out
