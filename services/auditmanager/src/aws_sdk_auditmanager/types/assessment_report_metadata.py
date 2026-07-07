"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_name
    import aws_sdk_auditmanager.types.assessment_report_description
    import aws_sdk_auditmanager.types.assessment_report_name
    import aws_sdk_auditmanager.types.assessment_report_status
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.username
    import aws_sdk_auditmanager.types.uuid


class AssessmentReportMetadata(TypedDict, closed=True):
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the assessment report. </p>"""
    name: NotRequired[
        "aws_sdk_auditmanager.types.assessment_report_name.AssessmentReportName"
    ]
    """<p> The name of the assessment report. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.assessment_report_description.AssessmentReportDescription"
    ]
    """<p> The description of the assessment report. </p>"""
    assessment_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the associated assessment. </p>"""
    assessment_name: NotRequired[
        "aws_sdk_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p>The name of the associated assessment. </p>"""
    author: NotRequired["aws_sdk_auditmanager.types.username.Username"]
    """<p> The name of the user who created the assessment report. </p>"""
    status: NotRequired[
        "aws_sdk_auditmanager.types.assessment_report_status.AssessmentReportStatus"
    ]
    """<p> The current status of the assessment report. </p>"""
    creation_time: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the assessment report was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "author" in value:
        out["author"] = value["author"]
    if "status" in value:
        import aws_sdk_auditmanager.types.assessment_report_status

        out["status"] = (
            aws_sdk_auditmanager.types.assessment_report_status.serialize_json(
                value["status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["creationTime"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentReportMetadata:
    out: AssessmentReportMetadata = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    if "author" in data:
        out["author"] = data["author"]
    if "status" in data:
        import aws_sdk_auditmanager.types.assessment_report_status

        out["status"] = (
            aws_sdk_auditmanager.types.assessment_report_status.deserialize_json(
                data["status"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["creation_time"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    return out
