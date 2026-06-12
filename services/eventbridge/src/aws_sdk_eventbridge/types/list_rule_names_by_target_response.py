"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListRuleNamesByTargetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.next_token
    import aws_sdk_eventbridge.types.rule_name_list


class ListRuleNamesByTargetResponse(TypedDict):
    rule_names: NotRequired["aws_sdk_eventbridge.types.rule_name_list.RuleNameList"]
    """<p>The names of the rules that can invoke the given target.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleNamesByTargetResponse) -> dict:
    out: dict = {}
    if "rule_names" in value:
        import aws_sdk_eventbridge.types.rule_name_list

        out["RuleNames"] = (
            aws_sdk_eventbridge.types.rule_name_list.serialize_aws_json_1_1(
                value["rule_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleNamesByTargetResponse:
    out: ListRuleNamesByTargetResponse = {}  # type: ignore[typeddict-item]
    if "RuleNames" in data:
        import aws_sdk_eventbridge.types.rule_name_list

        out["rule_names"] = (
            aws_sdk_eventbridge.types.rule_name_list.deserialize_aws_json_1_1(
                data["RuleNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
