"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessmentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.assessment_invoker
    import aws_sdk_resiliencehub.types.assessment_status
    import aws_sdk_resiliencehub.types.compliance_status
    import aws_sdk_resiliencehub.types.cost
    import aws_sdk_resiliencehub.types.double
    import aws_sdk_resiliencehub.types.drift_status
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.string500
    import aws_sdk_resiliencehub.types.time_stamp


class AppAssessmentSummary(TypedDict):
    app_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["aws_sdk_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version of an application.</p>"""
    assessment_status: "aws_sdk_resiliencehub.types.assessment_status.AssessmentStatus"
    """<p>Current status of the assessment for the resiliency policy.</p>"""
    invoker: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_invoker.AssessmentInvoker"
    ]
    """<p>Entity that invoked the assessment.</p>"""
    start_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Starting time for the action.</p>"""
    end_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>End time for the action.</p>"""
    message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Message from the assessment run.</p>"""
    assessment_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the assessment.</p>"""
    assessment_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    compliance_status: NotRequired[
        "aws_sdk_resiliencehub.types.compliance_status.ComplianceStatus"
    ]
    """<p>Current status of compliance for the resiliency policy.</p>"""
    cost: NotRequired["aws_sdk_resiliencehub.types.cost.Cost"]
    """<p>Cost for an application.</p>"""
    resiliency_score: "aws_sdk_resiliencehub.types.double.Double"
    """<p>Current resiliency score for the application.</p>"""
    version_name: NotRequired[
        "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    ]
    """<p>Name of an application version.</p>"""
    drift_status: NotRequired["aws_sdk_resiliencehub.types.drift_status.DriftStatus"]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessmentSummary) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    import aws_sdk_resiliencehub.types.assessment_status

    out["assessmentStatus"] = (
        aws_sdk_resiliencehub.types.assessment_status.serialize_json(
            value["assessment_status"]
        )
    )
    if "invoker" in value:
        import aws_sdk_resiliencehub.types.assessment_invoker

        out["invoker"] = aws_sdk_resiliencehub.types.assessment_invoker.serialize_json(
            value["invoker"]
        )
    if "start_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["startTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["endTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
            value["end_time"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    out["assessmentArn"] = value["assessment_arn"]
    if "compliance_status" in value:
        import aws_sdk_resiliencehub.types.compliance_status

        out["complianceStatus"] = (
            aws_sdk_resiliencehub.types.compliance_status.serialize_json(
                value["compliance_status"]
            )
        )
    if "cost" in value:
        import aws_sdk_resiliencehub.types.cost

        out["cost"] = aws_sdk_resiliencehub.types.cost.serialize_json(value["cost"])
    out["resiliencyScore"] = value.get("resiliency_score", 0)
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "drift_status" in value:
        import aws_sdk_resiliencehub.types.drift_status

        out["driftStatus"] = aws_sdk_resiliencehub.types.drift_status.serialize_json(
            value["drift_status"]
        )
    return out


def deserialize_json(data: dict) -> AppAssessmentSummary:
    out: AppAssessmentSummary = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    if "assessmentStatus" in data:
        import aws_sdk_resiliencehub.types.assessment_status

        out["assessment_status"] = (
            aws_sdk_resiliencehub.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    else:
        raise DeserializationError("AppAssessmentSummary.assessment_status required")
    if "invoker" in data:
        import aws_sdk_resiliencehub.types.assessment_invoker

        out["invoker"] = (
            aws_sdk_resiliencehub.types.assessment_invoker.deserialize_json(
                data["invoker"]
            )
        )
    if "startTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["start_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["end_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    if "message" in data:
        out["message"] = data["message"]
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    if "assessmentArn" in data:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError("AppAssessmentSummary.assessment_arn required")
    if "complianceStatus" in data:
        import aws_sdk_resiliencehub.types.compliance_status

        out["compliance_status"] = (
            aws_sdk_resiliencehub.types.compliance_status.deserialize_json(
                data["complianceStatus"]
            )
        )
    if "cost" in data:
        import aws_sdk_resiliencehub.types.cost

        out["cost"] = aws_sdk_resiliencehub.types.cost.deserialize_json(data["cost"])
    if "resiliencyScore" in data:
        out["resiliency_score"] = data["resiliencyScore"]
    else:
        out["resiliency_score"] = 0
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "driftStatus" in data:
        import aws_sdk_resiliencehub.types.drift_status

        out["drift_status"] = aws_sdk_resiliencehub.types.drift_status.deserialize_json(
            data["driftStatus"]
        )
    return out
