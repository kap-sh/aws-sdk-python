"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.boolean
    import aws_sdk_eventbridge.types.event_bus_name_or_arn
    import aws_sdk_eventbridge.types.rule_name


class DeleteRuleRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "aws_sdk_eventbridge.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    force: "aws_sdk_eventbridge.types.boolean.Boolean"
    """<p>If this is a managed rule, created by an Amazon Web Services service on your behalf, you must specify <code>Force</code> as <code>True</code> to delete the rule. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using <code>DescribeRule</code> or <code>ListRules</code> and checking the <code>ManagedBy</code> field of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    out["Force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRuleRequest:
    out: DeleteRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteRuleRequest.name required")
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    if "Force" in data:
        out["force"] = data["Force"]
    else:
        out["force"] = False
    return out
