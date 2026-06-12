"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_bus_name_or_arn
    import aws_sdk_cloudwatch_events.types.rule_name
    import aws_sdk_cloudwatch_events.types.target_list


class PutTargetsRequest(TypedDict):
    rule: "aws_sdk_cloudwatch_events.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    targets: "aws_sdk_cloudwatch_events.types.target_list.TargetList"
    """<p>The targets to update or add to the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTargetsRequest) -> dict:
    out: dict = {}
    out["Rule"] = value["rule"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    import aws_sdk_cloudwatch_events.types.target_list

    out["Targets"] = aws_sdk_cloudwatch_events.types.target_list.serialize_aws_json_1_1(
        value["targets"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutTargetsRequest:
    out: PutTargetsRequest = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        out["rule"] = data["Rule"]
    else:
        raise DeserializationError("PutTargetsRequest.rule required")
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    if "Targets" in data:
        import aws_sdk_cloudwatch_events.types.target_list

        out["targets"] = (
            aws_sdk_cloudwatch_events.types.target_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    else:
        raise DeserializationError("PutTargetsRequest.targets required")
    return out
