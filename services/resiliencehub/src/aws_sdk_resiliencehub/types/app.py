"""Generated from Smithy shape ``com.amazonaws.resiliencehub#App``."""

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
    import aws_sdk_resiliencehub.types.event_subscription_list
    import aws_sdk_resiliencehub.types.integer_optional
    import aws_sdk_resiliencehub.types.permission_model
    import aws_sdk_resiliencehub.types.tag_map
    import aws_sdk_resiliencehub.types.time_stamp


class App(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    name: "aws_sdk_resiliencehub.types.entity_name.EntityName"
    """<p>Name for the application.</p>"""
    description: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Optional description for an application.</p>"""
    policy_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    creation_time: "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    """<p>Date and time when the application was created.</p>"""
    status: NotRequired["aws_sdk_resiliencehub.types.app_status_type.AppStatusType"]
    """<p>Status of the application.</p>"""
    compliance_status: NotRequired[
        "aws_sdk_resiliencehub.types.app_compliance_status_type.AppComplianceStatusType"
    ]
    """<p>Current status of compliance for the resiliency policy.</p>"""
    last_app_compliance_evaluation_time: NotRequired[
        "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Date and time the most recent compliance evaluation.</p>"""
    resiliency_score: "aws_sdk_resiliencehub.types.double.Double"
    """<p>Current resiliency score for the application.</p>"""
    last_resiliency_score_evaluation_time: NotRequired[
        "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Date and time the most recent resiliency score evaluation.</p>"""
    tags: NotRequired["aws_sdk_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    assessment_schedule: NotRequired[
        "aws_sdk_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
    ]
    """<p>Assessment execution schedule with 'Daily' or 'Disabled' values. </p>"""
    permission_model: NotRequired[
        "aws_sdk_resiliencehub.types.permission_model.PermissionModel"
    ]
    """<p>Defines the roles and credentials that Resilience Hub would use while creating the application, importing its resources, and running an assessment.</p>"""
    event_subscriptions: NotRequired[
        "aws_sdk_resiliencehub.types.event_subscription_list.EventSubscriptionList"
    ]
    """<p>The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for <b>Drift detected</b> and <b>Scheduled assessment failure</b> events.</p>"""
    drift_status: NotRequired[
        "aws_sdk_resiliencehub.types.app_drift_status_type.AppDriftStatusType"
    ]
    """<p>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</p>"""
    last_drift_evaluation_time: NotRequired[
        "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Indicates the last time that a drift was evaluated.</p>"""
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
def serialize_json(value: App) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    import aws_sdk_resiliencehub.types.time_stamp

    out["creationTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
        value["creation_time"]
    )
    if "status" in value:
        import aws_sdk_resiliencehub.types.app_status_type

        out["status"] = aws_sdk_resiliencehub.types.app_status_type.serialize_json(
            value["status"]
        )
    if "compliance_status" in value:
        import aws_sdk_resiliencehub.types.app_compliance_status_type

        out["complianceStatus"] = (
            aws_sdk_resiliencehub.types.app_compliance_status_type.serialize_json(
                value["compliance_status"]
            )
        )
    if "last_app_compliance_evaluation_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["lastAppComplianceEvaluationTime"] = (
            aws_sdk_resiliencehub.types.time_stamp.serialize_json(
                value["last_app_compliance_evaluation_time"]
            )
        )
    out["resiliencyScore"] = value.get("resiliency_score", 0)
    if "last_resiliency_score_evaluation_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["lastResiliencyScoreEvaluationTime"] = (
            aws_sdk_resiliencehub.types.time_stamp.serialize_json(
                value["last_resiliency_score_evaluation_time"]
            )
        )
    if "tags" in value:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "assessment_schedule" in value:
        import aws_sdk_resiliencehub.types.app_assessment_schedule_type

        out["assessmentSchedule"] = (
            aws_sdk_resiliencehub.types.app_assessment_schedule_type.serialize_json(
                value["assessment_schedule"]
            )
        )
    if "permission_model" in value:
        import aws_sdk_resiliencehub.types.permission_model

        out["permissionModel"] = (
            aws_sdk_resiliencehub.types.permission_model.serialize_json(
                value["permission_model"]
            )
        )
    if "event_subscriptions" in value:
        import aws_sdk_resiliencehub.types.event_subscription_list

        out["eventSubscriptions"] = (
            aws_sdk_resiliencehub.types.event_subscription_list.serialize_json(
                value["event_subscriptions"]
            )
        )
    if "drift_status" in value:
        import aws_sdk_resiliencehub.types.app_drift_status_type

        out["driftStatus"] = (
            aws_sdk_resiliencehub.types.app_drift_status_type.serialize_json(
                value["drift_status"]
            )
        )
    if "last_drift_evaluation_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["lastDriftEvaluationTime"] = (
            aws_sdk_resiliencehub.types.time_stamp.serialize_json(
                value["last_drift_evaluation_time"]
            )
        )
    if "rto_in_secs" in value:
        out["rtoInSecs"] = value["rto_in_secs"]
    if "rpo_in_secs" in value:
        out["rpoInSecs"] = value["rpo_in_secs"]
    if "aws_application_arn" in value:
        out["awsApplicationArn"] = value["aws_application_arn"]
    return out


def deserialize_json(data: dict) -> App:
    out: App = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("App.app_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("App.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "creationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["creation_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("App.creation_time required")
    if "status" in data:
        import aws_sdk_resiliencehub.types.app_status_type

        out["status"] = aws_sdk_resiliencehub.types.app_status_type.deserialize_json(
            data["status"]
        )
    if "complianceStatus" in data:
        import aws_sdk_resiliencehub.types.app_compliance_status_type

        out["compliance_status"] = (
            aws_sdk_resiliencehub.types.app_compliance_status_type.deserialize_json(
                data["complianceStatus"]
            )
        )
    if "lastAppComplianceEvaluationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["last_app_compliance_evaluation_time"] = (
            aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
                data["lastAppComplianceEvaluationTime"]
            )
        )
    if "resiliencyScore" in data:
        out["resiliency_score"] = data["resiliencyScore"]
    else:
        out["resiliency_score"] = 0
    if "lastResiliencyScoreEvaluationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["last_resiliency_score_evaluation_time"] = (
            aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
                data["lastResiliencyScoreEvaluationTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if "assessmentSchedule" in data:
        import aws_sdk_resiliencehub.types.app_assessment_schedule_type

        out["assessment_schedule"] = (
            aws_sdk_resiliencehub.types.app_assessment_schedule_type.deserialize_json(
                data["assessmentSchedule"]
            )
        )
    if "permissionModel" in data:
        import aws_sdk_resiliencehub.types.permission_model

        out["permission_model"] = (
            aws_sdk_resiliencehub.types.permission_model.deserialize_json(
                data["permissionModel"]
            )
        )
    if "eventSubscriptions" in data:
        import aws_sdk_resiliencehub.types.event_subscription_list

        out["event_subscriptions"] = (
            aws_sdk_resiliencehub.types.event_subscription_list.deserialize_json(
                data["eventSubscriptions"]
            )
        )
    if "driftStatus" in data:
        import aws_sdk_resiliencehub.types.app_drift_status_type

        out["drift_status"] = (
            aws_sdk_resiliencehub.types.app_drift_status_type.deserialize_json(
                data["driftStatus"]
            )
        )
    if "lastDriftEvaluationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["last_drift_evaluation_time"] = (
            aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
                data["lastDriftEvaluationTime"]
            )
        )
    if "rtoInSecs" in data:
        out["rto_in_secs"] = data["rtoInSecs"]
    if "rpoInSecs" in data:
        out["rpo_in_secs"] = data["rpoInSecs"]
    if "awsApplicationArn" in data:
        out["aws_application_arn"] = data["awsApplicationArn"]
    return out
