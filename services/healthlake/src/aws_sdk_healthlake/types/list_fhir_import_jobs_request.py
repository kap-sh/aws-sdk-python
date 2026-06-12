"""Generated from Smithy shape ``com.amazonaws.healthlake#ListFHIRImportJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.job_name
    import aws_sdk_healthlake.types.job_status
    import aws_sdk_healthlake.types.max_results_integer
    import aws_sdk_healthlake.types.next_token
    import aws_sdk_healthlake.types.timestamp


class ListFHIRImportJobsRequest(TypedDict):
    datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId"
    """<p>Limits the response to the import job with the specified data store ID. </p>"""
    next_token: NotRequired["aws_sdk_healthlake.types.next_token.NextToken"]
    """<p>The pagination token used to identify the next page of results to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_healthlake.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>Limits the number of results returned for <code>ListFHIRImportJobs</code> to a maximum quantity specified by the user.</p>"""
    job_name: NotRequired["aws_sdk_healthlake.types.job_name.JobName"]
    """<p>Limits the response to the import job with the specified job name. </p>"""
    job_status: NotRequired["aws_sdk_healthlake.types.job_status.JobStatus"]
    """<p>Limits the response to the import job with the specified job status. </p>"""
    submitted_before: NotRequired["aws_sdk_healthlake.types.timestamp.Timestamp"]
    """<p>Limits the response to FHIR import jobs submitted before a user- specified date. </p>"""
    submitted_after: NotRequired["aws_sdk_healthlake.types.timestamp.Timestamp"]
    """<p>Limits the response to FHIR import jobs submitted after a user-specified date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFHIRImportJobsRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import aws_sdk_healthlake.types.job_status

        out["JobStatus"] = aws_sdk_healthlake.types.job_status.serialize_aws_json_1_0(
            value["job_status"]
        )
    if "submitted_before" in value:
        import aws_sdk_healthlake.types.timestamp

        out["SubmittedBefore"] = (
            aws_sdk_healthlake.types.timestamp.serialize_aws_json_1_0(
                value["submitted_before"]
            )
        )
    if "submitted_after" in value:
        import aws_sdk_healthlake.types.timestamp

        out["SubmittedAfter"] = (
            aws_sdk_healthlake.types.timestamp.serialize_aws_json_1_0(
                value["submitted_after"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFHIRImportJobsRequest:
    out: ListFHIRImportJobsRequest = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("ListFHIRImportJobsRequest.datastore_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_healthlake.types.job_status

        out["job_status"] = (
            aws_sdk_healthlake.types.job_status.deserialize_aws_json_1_0(
                data["JobStatus"]
            )
        )
    if "SubmittedBefore" in data:
        import aws_sdk_healthlake.types.timestamp

        out["submitted_before"] = (
            aws_sdk_healthlake.types.timestamp.deserialize_aws_json_1_0(
                data["SubmittedBefore"]
            )
        )
    if "SubmittedAfter" in data:
        import aws_sdk_healthlake.types.timestamp

        out["submitted_after"] = (
            aws_sdk_healthlake.types.timestamp.deserialize_aws_json_1_0(
                data["SubmittedAfter"]
            )
        )
    return out
