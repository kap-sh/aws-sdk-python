"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_assessment_schedule_type
    import aws_sdk_resiliencehub.types.app_compliance_status_type
    import aws_sdk_resiliencehub.types.app_drift_status_type
    import aws_sdk_resiliencehub.types.app_status_type
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.double
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.integer_optional
    import aws_sdk_resiliencehub.types.time_stamp


class AppSummary(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    name: "aws_sdk_resiliencehub.types.entity_name.EntityName"
    """<p>The name of the application.</p>"""
    description: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>The optional description for an app.</p>"""
    creation_time: "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    """<p>Date and time when the app was created.</p>"""
    compliance_status: NotRequired[
        "aws_sdk_resiliencehub.types.app_compliance_status_type.AppComplianceStatusType"
    ]
    """<p>The current status of compliance for the resiliency policy.</p>"""
    resiliency_score: "aws_sdk_resiliencehub.types.double.Double"
    """<p>The current resiliency score for the application.</p>"""
    assessment_schedule: NotRequired[
        "aws_sdk_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
    ]
    """<p> Assessment execution schedule with 'Daily' or 'Disabled' values. </p>"""
    status: NotRequired["aws_sdk_resiliencehub.types.app_status_type.AppStatusType"]
    """<p>Status of the application.</p>"""
    drift_status: NotRequired[
        "aws_sdk_resiliencehub.types.app_drift_status_type.AppDriftStatusType"
    ]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""
    last_app_compliance_evaluation_time: NotRequired[
        "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Date and time of the most recent compliance evaluation.</p>"""
    rto_in_secs: NotRequired[
        "aws_sdk_resiliencehub.types.integer_optional.IntegerOptional"
    ]
    """<p>Recovery Time Objective (RTO) in seconds.</p>"""
    rpo_in_secs: NotRequired[
        "aws_sdk_resiliencehub.types.integer_optional.IntegerOptional"
    ]
    """<p>Recovery Point Objective (RPO) in seconds.</p>"""
    aws_application_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppSummary) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_resiliencehub.types.time_stamp

    out["creationTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
        value["creation_time"]
    )
    if "compliance_status" in value:
        import aws_sdk_resiliencehub.types.app_compliance_status_type

        out["complianceStatus"] = (
            aws_sdk_resiliencehub.types.app_compliance_status_type.serialize_json(
                value["compliance_status"]
            )
        )
    out["resiliencyScore"] = value.get("resiliency_score", 0)
    if "assessment_schedule" in value:
        import aws_sdk_resiliencehub.types.app_assessment_schedule_type

        out["assessmentSchedule"] = (
            aws_sdk_resiliencehub.types.app_assessment_schedule_type.serialize_json(
                value["assessment_schedule"]
            )
        )
    if "status" in value:
        import aws_sdk_resiliencehub.types.app_status_type

        out["status"] = aws_sdk_resiliencehub.types.app_status_type.serialize_json(
            value["status"]
        )
    if "drift_status" in value:
        import aws_sdk_resiliencehub.types.app_drift_status_type

        out["driftStatus"] = (
            aws_sdk_resiliencehub.types.app_drift_status_type.serialize_json(
                value["drift_status"]
            )
        )
    if "last_app_compliance_evaluation_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["lastAppComplianceEvaluationTime"] = (
            aws_sdk_resiliencehub.types.time_stamp.serialize_json(
                value["last_app_compliance_evaluation_time"]
            )
        )
    if "rto_in_secs" in value:
        out["rtoInSecs"] = value["rto_in_secs"]
    if "rpo_in_secs" in value:
        out["rpoInSecs"] = value["rpo_in_secs"]
    if "aws_application_arn" in value:
        out["awsApplicationArn"] = value["aws_application_arn"]
    return out


def deserialize_json(data: dict) -> AppSummary:
    out: AppSummary = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("AppSummary.app_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AppSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["creation_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("AppSummary.creation_time required")
    if "complianceStatus" in data:
        import aws_sdk_resiliencehub.types.app_compliance_status_type

        out["compliance_status"] = (
            aws_sdk_resiliencehub.types.app_compliance_status_type.deserialize_json(
                data["complianceStatus"]
            )
        )
    if "resiliencyScore" in data:
        out["resiliency_score"] = data["resiliencyScore"]
    else:
        out["resiliency_score"] = 0
    if "assessmentSchedule" in data:
        import aws_sdk_resiliencehub.types.app_assessment_schedule_type

        out["assessment_schedule"] = (
            aws_sdk_resiliencehub.types.app_assessment_schedule_type.deserialize_json(
                data["assessmentSchedule"]
            )
        )
    if "status" in data:
        import aws_sdk_resiliencehub.types.app_status_type

        out["status"] = aws_sdk_resiliencehub.types.app_status_type.deserialize_json(
            data["status"]
        )
    if "driftStatus" in data:
        import aws_sdk_resiliencehub.types.app_drift_status_type

        out["drift_status"] = (
            aws_sdk_resiliencehub.types.app_drift_status_type.deserialize_json(
                data["driftStatus"]
            )
        )
    if "lastAppComplianceEvaluationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["last_app_compliance_evaluation_time"] = (
            aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
                data["lastAppComplianceEvaluationTime"]
            )
        )
    if "rtoInSecs" in data:
        out["rto_in_secs"] = data["rtoInSecs"]
    if "rpoInSecs" in data:
        out["rpo_in_secs"] = data["rpoInSecs"]
    if "awsApplicationArn" in data:
        out["aws_application_arn"] = data["awsApplicationArn"]
    return out
