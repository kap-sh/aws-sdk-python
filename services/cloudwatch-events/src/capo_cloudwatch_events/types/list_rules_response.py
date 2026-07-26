"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.next_token
    import capo_cloudwatch_events.types.rule_response_list


class ListRulesResponse(TypedDict, closed=True):
    rules: NotRequired[
        "capo_cloudwatch_events.types.rule_response_list.RuleResponseList"
    ]
    """<p>The rules that match the specified criteria.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If there are no more results, the value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_cloudwatch_events.types.rule_response_list

        out["Rules"] = (
            capo_cloudwatch_events.types.rule_response_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import capo_cloudwatch_events.types.rule_response_list

        out["rules"] = (
            capo_cloudwatch_events.types.rule_response_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
