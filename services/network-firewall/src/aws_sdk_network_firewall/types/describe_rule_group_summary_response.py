"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeRuleGroupSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.summary


class DescribeRuleGroupSummaryResponse(TypedDict, closed=True):
    rule_group_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the rule group. </p>"""
    summary: NotRequired["aws_sdk_network_firewall.types.summary.Summary"]
    """<p>A complex type that contains rule information based on the rule group's configured summary settings. The content varies depending on the fields that you specified to extract in your SummaryConfiguration. When you haven't configured any summary settings, this returns an empty array. The response might include:</p> <ul> <li> <p>Rule identifiers</p> </li> <li> <p>Rule descriptions</p> </li> <li> <p>Any metadata fields that you specified in your SummaryConfiguration</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRuleGroupSummaryResponse) -> dict:
    out: dict = {}
    out["RuleGroupName"] = value["rule_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "summary" in value:
        import aws_sdk_network_firewall.types.summary

        out["Summary"] = aws_sdk_network_firewall.types.summary.serialize_aws_json_1_0(
            value["summary"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRuleGroupSummaryResponse:
    out: DescribeRuleGroupSummaryResponse = {}  # type: ignore[typeddict-item]
    if "RuleGroupName" in data:
        out["rule_group_name"] = data["RuleGroupName"]
    else:
        raise DeserializationError(
            "DescribeRuleGroupSummaryResponse.rule_group_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Summary" in data:
        import aws_sdk_network_firewall.types.summary

        out["summary"] = (
            aws_sdk_network_firewall.types.summary.deserialize_aws_json_1_0(
                data["Summary"]
            )
        )
    return out
