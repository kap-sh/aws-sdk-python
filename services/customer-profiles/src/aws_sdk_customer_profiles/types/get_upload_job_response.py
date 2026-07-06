"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.expiration_days_integer
    import aws_sdk_customer_profiles.types.field_map
    import aws_sdk_customer_profiles.types.results_summary
    import aws_sdk_customer_profiles.types.status_reason
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.text
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.upload_job_status
    import aws_sdk_customer_profiles.types.uuid


class GetUploadJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of the upload job. </p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The unique name of the upload job. Could be a file name to identify the upload job. </p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.upload_job_status.UploadJobStatus"
    ]
    """<p>The status describing the status for the upload job. The following are Valid Values: </p> <ul> <li> <p> <b>CREATED</b>: The upload job has been created, but has not started processing yet. </p> </li> <li> <p> <b>IN_PROGRESS</b>: The upload job is currently in progress, ingesting and processing the profile data. </p> </li> <li> <p> <b>PARTIALLY_SUCCEEDED</b>: The upload job has successfully completed the ingestion and processing of all profile data. </p> </li> <li> <p> <b>SUCCEEDED</b>: The upload job has successfully completed the ingestion and processing of all profile data. </p> </li> <li> <p> <b>FAILED</b>: The upload job has failed to complete. </p> </li> <li> <p> <b>STOPPED</b>: The upload job has been manually stopped or terminated before completion. </p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_customer_profiles.types.status_reason.StatusReason"
    ]
    """<p>The reason for the current status of the upload job. Possible reasons: </p> <ul> <li> <p> <b>VALIDATION_FAILURE</b>: The upload job has encountered an error or issue and was unable to complete the profile data ingestion. </p> </li> <li> <p> <b>INTERNAL_FAILURE</b>: Failure caused from service side </p> </li> </ul>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the upload job was created. </p>"""
    completed_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the upload job was completed. </p>"""
    fields: NotRequired["aws_sdk_customer_profiles.types.field_map.FieldMap"]
    """<p>The mapping between CSV Columns and Profile Object attributes for the upload job. </p>"""
    unique_key: NotRequired["aws_sdk_customer_profiles.types.text.text"]
    """<p>The unique key columns used for de-duping the keys in the upload job. </p>"""
    results_summary: NotRequired[
        "aws_sdk_customer_profiles.types.results_summary.ResultsSummary"
    ]
    """<p>The summary of results for the upload job, including the number of updated, created, and failed records. </p>"""
    data_expiry: NotRequired[
        "aws_sdk_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
    ]
    """<p>The expiry duration for the profiles ingested with the upload job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobResponse) -> dict:
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
    if "fields" in value:
        import aws_sdk_customer_profiles.types.field_map

        out["Fields"] = aws_sdk_customer_profiles.types.field_map.serialize_json(
            value["fields"]
        )
    if "unique_key" in value:
        out["UniqueKey"] = value["unique_key"]
    if "results_summary" in value:
        import aws_sdk_customer_profiles.types.results_summary

        out["ResultsSummary"] = (
            aws_sdk_customer_profiles.types.results_summary.serialize_json(
                value["results_summary"]
            )
        )
    if "data_expiry" in value:
        out["DataExpiry"] = value["data_expiry"]
    return out


def deserialize_json(data: dict) -> GetUploadJobResponse:
    out: GetUploadJobResponse = {}  # type: ignore[typeddict-item]
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
    if "Fields" in data:
        import aws_sdk_customer_profiles.types.field_map

        out["fields"] = aws_sdk_customer_profiles.types.field_map.deserialize_json(
            data["Fields"]
        )
    if "UniqueKey" in data:
        out["unique_key"] = data["UniqueKey"]
    if "ResultsSummary" in data:
        import aws_sdk_customer_profiles.types.results_summary

        out["results_summary"] = (
            aws_sdk_customer_profiles.types.results_summary.deserialize_json(
                data["ResultsSummary"]
            )
        )
    if "DataExpiry" in data:
        out["data_expiry"] = data["DataExpiry"]
    return out
