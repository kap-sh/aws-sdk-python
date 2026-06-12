"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_assessment_schedule_type
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.boolean_optional
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.event_subscription_list
    import aws_sdk_resiliencehub.types.permission_model


class UpdateAppRequest(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    description: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>The optional description for an app.</p>"""
    policy_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    clear_resiliency_policy_arn: NotRequired[
        "aws_sdk_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies if the resiliency policy ARN should be cleared.</p>"""
    assessment_schedule: NotRequired[
        "aws_sdk_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
    ]
    """<p> Assessment execution schedule with 'Daily' or 'Disabled' values. </p>"""
    permission_model: NotRequired[
        "aws_sdk_resiliencehub.types.permission_model.PermissionModel"
    ]
    """<p>Defines the roles and credentials that Resilience Hub would use while creating an application, importing its resources, and running an assessment.</p>"""
    event_subscriptions: NotRequired[
        "aws_sdk_resiliencehub.types.event_subscription_list.EventSubscriptionList"
    ]
    """<p>The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for <b>Drift detected</b> and <b>Scheduled assessment failure</b> events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "clear_resiliency_policy_arn" in value:
        out["clearResiliencyPolicyArn"] = value["clear_resiliency_policy_arn"]
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
    return out


def deserialize_json(data: dict) -> UpdateAppRequest:
    out: UpdateAppRequest = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("UpdateAppRequest.app_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "clearResiliencyPolicyArn" in data:
        out["clear_resiliency_policy_arn"] = data["clearResiliencyPolicyArn"]
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
    return out
