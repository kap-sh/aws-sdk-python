"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_security_group_rules_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.security_group_rule_id_list
    import aws_sdk_ec2.types.string


class DescribeSecurityGroupRulesRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>group-id</code> - The ID of the security group.</p> </li> <li> <p> <code>security-group-rule-id</code> - The ID of the security group rule.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> </ul>"""
    security_group_rule_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id_list.SecurityGroupRuleIdList"
    ]
    """<p>The IDs of the security group rules.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_security_group_rules_max_results.DescribeSecurityGroupRulesMaxResults"
    ]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. This value can be between 5 and 1000. If this parameter is not specified, then all items are returned. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupRulesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "security_group_rule_ids" in value:
        import aws_sdk_ec2.types.security_group_rule_id_list

        aws_sdk_ec2.types.security_group_rule_id_list.serialize_ec2_query(
            value["security_group_rule_ids"], pairs, f"{prefix}.SecurityGroupRuleIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupRulesRequest:
    out: DescribeSecurityGroupRulesRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    if el.find("SecurityGroupRuleIds") is not None:
        import aws_sdk_ec2.types.security_group_rule_id_list

        out["security_group_rule_ids"] = (
            aws_sdk_ec2.types.security_group_rule_id_list.deserialize_ec2_query(
                el, "SecurityGroupRuleIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
