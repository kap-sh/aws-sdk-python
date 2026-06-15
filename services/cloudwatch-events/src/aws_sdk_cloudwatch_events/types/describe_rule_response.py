"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.created_by
    import aws_sdk_cloudwatch_events.types.event_bus_name
    import aws_sdk_cloudwatch_events.types.event_pattern
    import aws_sdk_cloudwatch_events.types.managed_by
    import aws_sdk_cloudwatch_events.types.role_arn
    import aws_sdk_cloudwatch_events.types.rule_arn
    import aws_sdk_cloudwatch_events.types.rule_description
    import aws_sdk_cloudwatch_events.types.rule_name
    import aws_sdk_cloudwatch_events.types.rule_state
    import aws_sdk_cloudwatch_events.types.schedule_expression


class DescribeRuleResponse(TypedDict):
    name: NotRequired["aws_sdk_cloudwatch_events.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    arn: NotRequired["aws_sdk_cloudwatch_events.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    event_pattern: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_pattern.EventPattern"
    ]
    r"""<p>The event pattern. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html\">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    schedule_expression: NotRequired[
        "aws_sdk_cloudwatch_events.types.schedule_expression.ScheduleExpression"
    ]
    r"""<p>The scheduling expression. For example, \"cron(0 20 * * ? *)\", \"rate(5 minutes)\".</p>"""
    state: NotRequired["aws_sdk_cloudwatch_events.types.rule_state.RuleState"]
    """<p>Specifies whether the rule is enabled or disabled.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_events.types.rule_description.RuleDescription"
    ]
    """<p>The description of the rule.</p>"""
    role_arn: NotRequired["aws_sdk_cloudwatch_events.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the rule.</p>"""
    managed_by: NotRequired["aws_sdk_cloudwatch_events.types.managed_by.ManagedBy"]
    """<p>If this is a managed rule, created by an Amazon Web Services service on your behalf, this field displays the principal name of the Amazon Web Services service that created the rule.</p>"""
    event_bus_name: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_bus_name.EventBusName"
    ]
    """<p>The name of the event bus associated with the rule.</p>"""
    created_by: NotRequired["aws_sdk_cloudwatch_events.types.created_by.CreatedBy"]
    """<p>The account ID of the user that created the rule. If you use <code>PutRule</code> to put a rule on an event bus in another account, the other account is the owner of the rule, and the rule ARN includes the account ID for that account. However, the value for <code>CreatedBy</code> is the account ID as the account that created the rule in the other account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRuleResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "state" in value:
        import aws_sdk_cloudwatch_events.types.rule_state

        out["State"] = (
            aws_sdk_cloudwatch_events.types.rule_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "managed_by" in value:
        out["ManagedBy"] = value["managed_by"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRuleResponse:
    out: DescribeRuleResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "EventPattern" in data:
        out["event_pattern"] = data["EventPattern"]
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "State" in data:
        import aws_sdk_cloudwatch_events.types.rule_state

        out["state"] = (
            aws_sdk_cloudwatch_events.types.rule_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ManagedBy" in data:
        out["managed_by"] = data["ManagedBy"]
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    return out
