"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.assessment_compliance
    import aws_sdk_resiliencehub.types.assessment_invoker
    import aws_sdk_resiliencehub.types.assessment_status
    import aws_sdk_resiliencehub.types.assessment_summary
    import aws_sdk_resiliencehub.types.compliance_status
    import aws_sdk_resiliencehub.types.cost
    import aws_sdk_resiliencehub.types.drift_status
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.resiliency_policy
    import aws_sdk_resiliencehub.types.resiliency_score
    import aws_sdk_resiliencehub.types.resource_errors_details
    import aws_sdk_resiliencehub.types.string500
    import aws_sdk_resiliencehub.types.tag_map
    import aws_sdk_resiliencehub.types.time_stamp


class AppAssessment(TypedDict, closed=True):
    app_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["aws_sdk_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version of an application.</p>"""
    invoker: "aws_sdk_resiliencehub.types.assessment_invoker.AssessmentInvoker"
    """<p>The entity that invoked the assessment.</p>"""
    cost: NotRequired["aws_sdk_resiliencehub.types.cost.Cost"]
    """<p>Cost for the application.</p>"""
    resiliency_score: NotRequired[
        "aws_sdk_resiliencehub.types.resiliency_score.ResiliencyScore"
    ]
    """<p>Current resiliency score for an application.</p>"""
    compliance: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>Application compliance against the resiliency policy.</p>"""
    compliance_status: NotRequired[
        "aws_sdk_resiliencehub.types.compliance_status.ComplianceStatus"
    ]
    """<p>Current status of the compliance for the resiliency policy.</p>"""
    assessment_status: "aws_sdk_resiliencehub.types.assessment_status.AssessmentStatus"
    """<p>Current status of the assessment for the resiliency policy.</p>"""
    start_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Starting time for the action.</p>"""
    end_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>End time for the action.</p>"""
    message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Error or warning message from the assessment execution</p>"""
    assessment_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the assessment.</p>"""
    assessment_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    policy: NotRequired[
        "aws_sdk_resiliencehub.types.resiliency_policy.ResiliencyPolicy"
    ]
    """<p>Resiliency policy of an application.</p>"""
    tags: NotRequired["aws_sdk_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    resource_errors_details: NotRequired[
        "aws_sdk_resiliencehub.types.resource_errors_details.ResourceErrorsDetails"
    ]
    """<p> A resource error object containing a list of errors retrieving an application's resources. </p>"""
    version_name: NotRequired[
        "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    ]
    """<p>Version name of the published application.</p>"""
    drift_status: NotRequired["aws_sdk_resiliencehub.types.drift_status.DriftStatus"]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""
    summary: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_summary.AssessmentSummary"
    ]
    """<p>Indicates the AI-generated summary for the Resilience Hub assessment, providing a concise overview that highlights the top risks and recommendations.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessment) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    import aws_sdk_resiliencehub.types.assessment_invoker

    out["invoker"] = aws_sdk_resiliencehub.types.assessment_invoker.serialize_json(
        value["invoker"]
    )
    if "cost" in value:
        import aws_sdk_resiliencehub.types.cost

        out["cost"] = aws_sdk_resiliencehub.types.cost.serialize_json(value["cost"])
    if "resiliency_score" in value:
        import aws_sdk_resiliencehub.types.resiliency_score

        out["resiliencyScore"] = (
            aws_sdk_resiliencehub.types.resiliency_score.serialize_json(
                value["resiliency_score"]
            )
        )
    if "compliance" in value:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.serialize_json(
                value["compliance"]
            )
        )
    if "compliance_status" in value:
        import aws_sdk_resiliencehub.types.compliance_status

        out["complianceStatus"] = (
            aws_sdk_resiliencehub.types.compliance_status.serialize_json(
                value["compliance_status"]
            )
        )
    import aws_sdk_resiliencehub.types.assessment_status

    out["assessmentStatus"] = (
        aws_sdk_resiliencehub.types.assessment_status.serialize_json(
            value["assessment_status"]
        )
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
    if "policy" in value:
        import aws_sdk_resiliencehub.types.resiliency_policy

        out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.serialize_json(
            value["policy"]
        )
    if "tags" in value:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "resource_errors_details" in value:
        import aws_sdk_resiliencehub.types.resource_errors_details

        out["resourceErrorsDetails"] = (
            aws_sdk_resiliencehub.types.resource_errors_details.serialize_json(
                value["resource_errors_details"]
            )
        )
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "drift_status" in value:
        import aws_sdk_resiliencehub.types.drift_status

        out["driftStatus"] = aws_sdk_resiliencehub.types.drift_status.serialize_json(
            value["drift_status"]
        )
    if "summary" in value:
        import aws_sdk_resiliencehub.types.assessment_summary

        out["summary"] = aws_sdk_resiliencehub.types.assessment_summary.serialize_json(
            value["summary"]
        )
    return out


def deserialize_json(data: dict) -> AppAssessment:
    out: AppAssessment = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    if "invoker" in data:
        import aws_sdk_resiliencehub.types.assessment_invoker

        out["invoker"] = (
            aws_sdk_resiliencehub.types.assessment_invoker.deserialize_json(
                data["invoker"]
            )
        )
    else:
        raise DeserializationError("AppAssessment.invoker required")
    if "cost" in data:
        import aws_sdk_resiliencehub.types.cost

        out["cost"] = aws_sdk_resiliencehub.types.cost.deserialize_json(data["cost"])
    if "resiliencyScore" in data:
        import aws_sdk_resiliencehub.types.resiliency_score

        out["resiliency_score"] = (
            aws_sdk_resiliencehub.types.resiliency_score.deserialize_json(
                data["resiliencyScore"]
            )
        )
    if "compliance" in data:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.deserialize_json(
                data["compliance"]
            )
        )
    if "complianceStatus" in data:
        import aws_sdk_resiliencehub.types.compliance_status

        out["compliance_status"] = (
            aws_sdk_resiliencehub.types.compliance_status.deserialize_json(
                data["complianceStatus"]
            )
        )
    if "assessmentStatus" in data:
        import aws_sdk_resiliencehub.types.assessment_status

        out["assessment_status"] = (
            aws_sdk_resiliencehub.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    else:
        raise DeserializationError("AppAssessment.assessment_status required")
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
        raise DeserializationError("AppAssessment.assessment_arn required")
    if "policy" in data:
        import aws_sdk_resiliencehub.types.resiliency_policy

        out["policy"] = aws_sdk_resiliencehub.types.resiliency_policy.deserialize_json(
            data["policy"]
        )
    if "tags" in data:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if "resourceErrorsDetails" in data:
        import aws_sdk_resiliencehub.types.resource_errors_details

        out["resource_errors_details"] = (
            aws_sdk_resiliencehub.types.resource_errors_details.deserialize_json(
                data["resourceErrorsDetails"]
            )
        )
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "driftStatus" in data:
        import aws_sdk_resiliencehub.types.drift_status

        out["drift_status"] = aws_sdk_resiliencehub.types.drift_status.deserialize_json(
            data["driftStatus"]
        )
    if "summary" in data:
        import aws_sdk_resiliencehub.types.assessment_summary

        out["summary"] = (
            aws_sdk_resiliencehub.types.assessment_summary.deserialize_json(
                data["summary"]
            )
        )
    return out
