"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLastAccessedDetailsWithEntitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.entity_details_list_type
    import aws_sdk_iam.types.error_details
    import aws_sdk_iam.types.job_status_type
    import aws_sdk_iam.types.response_marker_type


class GetServiceLastAccessedDetailsWithEntitiesResponse(TypedDict):
    job_status: "aws_sdk_iam.types.job_status_type.jobStatusType"
    """<p>The status of the job.</p>"""
    job_creation_date: "aws_sdk_iam.types.date_type.dateType"
    r"""<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the report job was created.</p>"""
    job_completion_date: "aws_sdk_iam.types.date_type.dateType"
    r"""<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the generated report job was completed or failed.</p> <p>This field is null if the job is still in progress, as indicated by a job status value of <code>IN_PROGRESS</code>.</p>"""
    entity_details_list: (
        "aws_sdk_iam.types.entity_details_list_type.entityDetailsListType"
    )
    """<p>An <code>EntityDetailsList</code> object that contains details about when an IAM entity (user or role) used group or policy permissions in an attempt to access the specified Amazon Web Services service.</p>"""
    is_truncated: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["aws_sdk_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""
    error: NotRequired["aws_sdk_iam.types.error_details.ErrorDetails"]
    """<p>An object that contains details about the reason the operation failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetServiceLastAccessedDetailsWithEntitiesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_iam.types.job_status_type

    aws_sdk_iam.types.job_status_type.serialize_query(
        value["job_status"], pairs, f"{prefix}.JobStatus"
    )
    import aws_sdk_iam.types.date_type

    aws_sdk_iam.types.date_type.serialize_query(
        value["job_creation_date"], pairs, f"{prefix}.JobCreationDate"
    )
    import aws_sdk_iam.types.date_type

    aws_sdk_iam.types.date_type.serialize_query(
        value["job_completion_date"], pairs, f"{prefix}.JobCompletionDate"
    )
    import aws_sdk_iam.types.entity_details_list_type

    aws_sdk_iam.types.entity_details_list_type.serialize_query(
        value["entity_details_list"], pairs, f"{prefix}.EntityDetailsList"
    )
    pairs.append(
        (
            f"{prefix}.IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "error" in value:
        import aws_sdk_iam.types.error_details

        aws_sdk_iam.types.error_details.serialize_query(
            value["error"], pairs, f"{prefix}.Error"
        )


def deserialize_query(el: Element) -> GetServiceLastAccessedDetailsWithEntitiesResponse:
    out: GetServiceLastAccessedDetailsWithEntitiesResponse = {}  # type: ignore[typeddict-item]
    child_job_status = el.find("JobStatus")
    if child_job_status is not None:
        import aws_sdk_iam.types.job_status_type

        out["job_status"] = aws_sdk_iam.types.job_status_type.deserialize_query(
            child_job_status
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsWithEntitiesResponse.job_status required"
        )
    child_job_creation_date = el.find("JobCreationDate")
    if child_job_creation_date is not None:
        import aws_sdk_iam.types.date_type

        out["job_creation_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_job_creation_date
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsWithEntitiesResponse.job_creation_date required"
        )
    child_job_completion_date = el.find("JobCompletionDate")
    if child_job_completion_date is not None:
        import aws_sdk_iam.types.date_type

        out["job_completion_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_job_completion_date
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsWithEntitiesResponse.job_completion_date required"
        )
    child_entity_details_list = el.find("EntityDetailsList")
    if child_entity_details_list is not None:
        import aws_sdk_iam.types.entity_details_list_type

        out["entity_details_list"] = (
            aws_sdk_iam.types.entity_details_list_type.deserialize_query(
                child_entity_details_list
            )
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsWithEntitiesResponse.entity_details_list required"
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_error = el.find("Error")
    if child_error is not None:
        import aws_sdk_iam.types.error_details

        out["error"] = aws_sdk_iam.types.error_details.deserialize_query(child_error)
    return out
