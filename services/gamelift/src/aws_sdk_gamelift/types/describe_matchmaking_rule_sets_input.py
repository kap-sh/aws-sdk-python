"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingRuleSetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_rule_set_name_list
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.rule_set_limit


class DescribeMatchmakingRuleSetsInput(TypedDict, closed=True):
    names: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_rule_set_name_list.MatchmakingRuleSetNameList"
    ]
    r"""<p>A list of one or more matchmaking rule set names to retrieve details for. (Note: The rule set name is different from the optional \"name\" field in the rule set body.) You can use either the rule set name or ARN value. </p>"""
    limit: NotRequired["aws_sdk_gamelift.types.rule_set_limit.RuleSetLimit"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingRuleSetsInput) -> dict:
    out: dict = {}
    if "names" in value:
        import aws_sdk_gamelift.types.matchmaking_rule_set_name_list

        out["Names"] = (
            aws_sdk_gamelift.types.matchmaking_rule_set_name_list.serialize_aws_json_1_1(
                value["names"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingRuleSetsInput:
    out: DescribeMatchmakingRuleSetsInput = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import aws_sdk_gamelift.types.matchmaking_rule_set_name_list

        out["names"] = (
            aws_sdk_gamelift.types.matchmaking_rule_set_name_list.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
