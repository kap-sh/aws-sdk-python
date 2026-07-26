"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_name_or_arn
    import capo_cloudwatch_events.types.limit_max100
    import capo_cloudwatch_events.types.next_token
    import capo_cloudwatch_events.types.rule_name


class ListRulesRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_cloudwatch_events.types.rule_name.RuleName"]
    """<p>The prefix matching the rule name.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus to list the rules for. If you omit this, the default event bus is used.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    limit: NotRequired["capo_cloudwatch_events.types.limit_max100.LimitMax100"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesRequest:
    out: ListRulesRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
