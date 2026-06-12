"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RemoveTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.boolean
    import aws_sdk_cloudwatch_events.types.event_bus_name_or_arn
    import aws_sdk_cloudwatch_events.types.rule_name
    import aws_sdk_cloudwatch_events.types.target_id_list


class RemoveTargetsRequest(TypedDict):
    rule: "aws_sdk_cloudwatch_events.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    ids: "aws_sdk_cloudwatch_events.types.target_id_list.TargetIdList"
    """<p>The IDs of the targets to remove from the rule.</p>"""
    force: "aws_sdk_cloudwatch_events.types.boolean.Boolean"
    """<p>If this is a managed rule, created by an Amazon Web Services service on your behalf, you must specify <code>Force</code> as <code>True</code> to remove targets. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using <code>DescribeRule</code> or <code>ListRules</code> and checking the <code>ManagedBy</code> field of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTargetsRequest) -> dict:
    out: dict = {}
    out["Rule"] = value["rule"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    import aws_sdk_cloudwatch_events.types.target_id_list

    out["Ids"] = aws_sdk_cloudwatch_events.types.target_id_list.serialize_aws_json_1_1(
        value["ids"]
    )
    out["Force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTargetsRequest:
    out: RemoveTargetsRequest = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        out["rule"] = data["Rule"]
    else:
        raise DeserializationError("RemoveTargetsRequest.rule required")
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    if "Ids" in data:
        import aws_sdk_cloudwatch_events.types.target_id_list

        out["ids"] = (
            aws_sdk_cloudwatch_events.types.target_id_list.deserialize_aws_json_1_1(
                data["Ids"]
            )
        )
    else:
        raise DeserializationError("RemoveTargetsRequest.ids required")
    if "Force" in data:
        out["force"] = data["Force"]
    else:
        out["force"] = False
    return out
