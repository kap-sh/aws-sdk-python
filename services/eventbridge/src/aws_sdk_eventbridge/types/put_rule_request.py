"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_bus_name_or_arn
    import aws_sdk_eventbridge.types.event_pattern
    import aws_sdk_eventbridge.types.role_arn
    import aws_sdk_eventbridge.types.rule_description
    import aws_sdk_eventbridge.types.rule_name
    import aws_sdk_eventbridge.types.rule_state
    import aws_sdk_eventbridge.types.schedule_expression
    import aws_sdk_eventbridge.types.tag_list


class PutRuleRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.rule_name.RuleName"
    """<p>The name of the rule that you are creating or updating.</p>"""
    schedule_expression: NotRequired[
        "aws_sdk_eventbridge.types.schedule_expression.ScheduleExpression"
    ]
    r"""<p>The scheduling expression. For example, \"cron(0 20 * * ? *)\" or \"rate(5 minutes)\".</p>"""
    event_pattern: NotRequired["aws_sdk_eventbridge.types.event_pattern.EventPattern"]
    r"""<p>The event pattern. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.rule_state.RuleState"]
    r"""<p>The state of the rule.</p> <p>Valid values include:</p> <ul> <li> <p> <code>DISABLED</code>: The rule is disabled. EventBridge does not match any events against the rule.</p> </li> <li> <p> <code>ENABLED</code>: The rule is enabled. EventBridge matches events against the rule, <i>except</i> for Amazon Web Services management events delivered through CloudTrail.</p> </li> <li> <p> <code>ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS</code>: The rule is enabled for all events, including Amazon Web Services management events delivered through CloudTrail.</p> <p>Management events provide visibility into management operations that are performed on resources in your Amazon Web Services account. These are also known as control plane operations. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events\">Logging management events</a> in the <i>CloudTrail User Guide</i>, and <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-cloudtrail\">Filtering management events from Amazon Web Services services</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p> <p>This value is only valid for rules on the <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html#eb-bus-concepts-buses\">default</a> event bus or <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html\">custom event buses</a>. It does not apply to <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html\">partner event buses</a>.</p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.rule_description.RuleDescription"
    ]
    """<p>A description of the rule.</p>"""
    role_arn: NotRequired["aws_sdk_eventbridge.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the rule.</p> <p>If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure, instead of here in this parameter.</p>"""
    tags: NotRequired["aws_sdk_eventbridge.types.tag_list.TagList"]
    """<p>The list of key-value pairs to associate with the rule.</p>"""
    event_bus_name: NotRequired[
        "aws_sdk_eventbridge.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus to associate with this rule. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "state" in value:
        import aws_sdk_eventbridge.types.rule_state

        out["State"] = aws_sdk_eventbridge.types.rule_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_eventbridge.types.tag_list

        out["Tags"] = aws_sdk_eventbridge.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRuleRequest:
    out: PutRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutRuleRequest.name required")
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "EventPattern" in data:
        out["event_pattern"] = data["EventPattern"]
    if "State" in data:
        import aws_sdk_eventbridge.types.rule_state

        out["state"] = aws_sdk_eventbridge.types.rule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import aws_sdk_eventbridge.types.tag_list

        out["tags"] = aws_sdk_eventbridge.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    return out
