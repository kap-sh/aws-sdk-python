"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListRuleNamesByTargetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.next_token
    import aws_sdk_cloudwatch_events.types.rule_name_list


class ListRuleNamesByTargetResponse(TypedDict):
    rule_names: NotRequired[
        "aws_sdk_cloudwatch_events.types.rule_name_list.RuleNameList"
    ]
    """<p>The names of the rules that can invoke the given target.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If there are no more results, the value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleNamesByTargetResponse) -> dict:
    out: dict = {}
    if "rule_names" in value:
        import aws_sdk_cloudwatch_events.types.rule_name_list

        out["RuleNames"] = (
            aws_sdk_cloudwatch_events.types.rule_name_list.serialize_aws_json_1_1(
                value["rule_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleNamesByTargetResponse:
    out: ListRuleNamesByTargetResponse = {}  # type: ignore[typeddict-item]
    if "RuleNames" in data:
        import aws_sdk_cloudwatch_events.types.rule_name_list

        out["rule_names"] = (
            aws_sdk_cloudwatch_events.types.rule_name_list.deserialize_aws_json_1_1(
                data["RuleNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
