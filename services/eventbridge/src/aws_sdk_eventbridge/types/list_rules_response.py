"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.next_token
    import aws_sdk_eventbridge.types.rule_response_list


class ListRulesResponse(TypedDict, closed=True):
    rules: NotRequired["aws_sdk_eventbridge.types.rule_response_list.RuleResponseList"]
    """<p>The rules that match the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_eventbridge.types.rule_response_list

        out["Rules"] = (
            aws_sdk_eventbridge.types.rule_response_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_eventbridge.types.rule_response_list

        out["rules"] = (
            aws_sdk_eventbridge.types.rule_response_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
