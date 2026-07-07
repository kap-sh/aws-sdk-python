"""Generated from Smithy shape ``com.amazonaws.eventbridge#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_bus_name
    import aws_sdk_eventbridge.types.event_pattern
    import aws_sdk_eventbridge.types.managed_by
    import aws_sdk_eventbridge.types.role_arn
    import aws_sdk_eventbridge.types.rule_arn
    import aws_sdk_eventbridge.types.rule_description
    import aws_sdk_eventbridge.types.rule_name
    import aws_sdk_eventbridge.types.rule_state
    import aws_sdk_eventbridge.types.schedule_expression


class Rule(TypedDict, closed=True):
    name: NotRequired["aws_sdk_eventbridge.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    arn: NotRequired["aws_sdk_eventbridge.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    event_pattern: NotRequired["aws_sdk_eventbridge.types.event_pattern.EventPattern"]
    r"""<p>The event pattern of the rule. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html\">Events and Event Patterns</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.rule_state.RuleState"]
    r"""<p>The state of the rule.</p> <p>Valid values include:</p> <ul> <li> <p> <code>DISABLED</code>: The rule is disabled. EventBridge does not match any events against the rule.</p> </li> <li> <p> <code>ENABLED</code>: The rule is enabled. EventBridge matches events against the rule, <i>except</i> for Amazon Web Services management events delivered through CloudTrail.</p> </li> <li> <p> <code>ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS</code>: The rule is enabled for all events, including Amazon Web Services management events delivered through CloudTrail.</p> <p>Management events provide visibility into management operations that are performed on resources in your Amazon Web Services account. These are also known as control plane operations. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events\">Logging management events</a> in the <i>CloudTrail User Guide</i>, and <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-cloudtrail\">Filtering management events from Amazon Web Services services</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p> <p>This value is only valid for rules on the <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html#eb-bus-concepts-buses\">default</a> event bus or <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html\">custom event buses</a>. It does not apply to <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html\">partner event buses</a>.</p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.rule_description.RuleDescription"
    ]
    """<p>The description of the rule.</p>"""
    schedule_expression: NotRequired[
        "aws_sdk_eventbridge.types.schedule_expression.ScheduleExpression"
    ]
    r"""<p>The scheduling expression. For example, \"cron(0 20 * * ? *)\", \"rate(5 minutes)\". For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html\">Creating an Amazon EventBridge rule that runs on a schedule</a>.</p>"""
    role_arn: NotRequired["aws_sdk_eventbridge.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role that is used for target invocation.</p> <p>If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure, instead of here in this parameter.</p>"""
    managed_by: NotRequired["aws_sdk_eventbridge.types.managed_by.ManagedBy"]
    """<p>If the rule was created on behalf of your account by an Amazon Web Services service, this field displays the principal name of the service that created the rule.</p>"""
    event_bus_name: NotRequired["aws_sdk_eventbridge.types.event_bus_name.EventBusName"]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "state" in value:
        import aws_sdk_eventbridge.types.rule_state

        out["State"] = aws_sdk_eventbridge.types.rule_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "managed_by" in value:
        out["ManagedBy"] = value["managed_by"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "EventPattern" in data:
        out["event_pattern"] = data["EventPattern"]
    if "State" in data:
        import aws_sdk_eventbridge.types.rule_state

        out["state"] = aws_sdk_eventbridge.types.rule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ManagedBy" in data:
        out["managed_by"] = data["ManagedBy"]
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    return out
