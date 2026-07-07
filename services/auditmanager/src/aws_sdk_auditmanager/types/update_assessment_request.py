"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_description
    import aws_sdk_auditmanager.types.assessment_name
    import aws_sdk_auditmanager.types.assessment_reports_destination
    import aws_sdk_auditmanager.types.roles
    import aws_sdk_auditmanager.types.scope
    import aws_sdk_auditmanager.types.uuid


class UpdateAssessmentRequest(TypedDict, closed=True):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    assessment_name: NotRequired[
        "aws_sdk_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p> The name of the assessment to be updated. </p>"""
    assessment_description: NotRequired[
        "aws_sdk_auditmanager.types.assessment_description.AssessmentDescription"
    ]
    """<p> The description of the assessment. </p>"""
    scope: "aws_sdk_auditmanager.types.scope.Scope"
    """<p> The scope of the assessment. </p>"""
    assessment_reports_destination: NotRequired[
        "aws_sdk_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p> The assessment report storage destination for the assessment that's being updated. </p>"""
    roles: NotRequired["aws_sdk_auditmanager.types.roles.Roles"]
    """<p> The list of roles for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentRequest) -> dict:
    out: dict = {}
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "assessment_description" in value:
        out["assessmentDescription"] = value["assessment_description"]
    import aws_sdk_auditmanager.types.scope

    out["scope"] = aws_sdk_auditmanager.types.scope.serialize_json(value["scope"])
    if "assessment_reports_destination" in value:
        import aws_sdk_auditmanager.types.assessment_reports_destination

        out["assessmentReportsDestination"] = (
            aws_sdk_auditmanager.types.assessment_reports_destination.serialize_json(
                value["assessment_reports_destination"]
            )
        )
    if "roles" in value:
        import aws_sdk_auditmanager.types.roles

        out["roles"] = aws_sdk_auditmanager.types.roles.serialize_json(value["roles"])
    return out


def deserialize_json(data: dict) -> UpdateAssessmentRequest:
    out: UpdateAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    if "assessmentDescription" in data:
        out["assessment_description"] = data["assessmentDescription"]
    if "scope" in data:
        import aws_sdk_auditmanager.types.scope

        out["scope"] = aws_sdk_auditmanager.types.scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("UpdateAssessmentRequest.scope required")
    if "assessmentReportsDestination" in data:
        import aws_sdk_auditmanager.types.assessment_reports_destination

        out["assessment_reports_destination"] = (
            aws_sdk_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["assessmentReportsDestination"]
            )
        )
    if "roles" in data:
        import aws_sdk_auditmanager.types.roles

        out["roles"] = aws_sdk_auditmanager.types.roles.deserialize_json(data["roles"])
    return out
