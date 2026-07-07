"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeInsightRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_max_results
    import aws_sdk_cloudwatch.types.next_token


class DescribeInsightRulesInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of rules.</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_max_results.InsightRuleMaxResults"
    ]
    """<p>The maximum number of results to return in one operation. If you omit this parameter, the default of 500 is used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeInsightRulesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeInsightRulesInput:
    out: DescribeInsightRulesInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInsightRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> DescribeInsightRulesInput:
    out: DescribeInsightRulesInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
