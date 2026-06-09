"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverRulesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set
    import aws_sdk_ec2.types.next_token


class GetIpamPrefixListResolverRulesResult(TypedDict):
    rules: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set.IpamPrefixListResolverRuleSet"
    ]
    """<p>The CIDR selection rules for the IPAM prefix list resolver.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPrefixListResolverRulesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "rules" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set

        aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set.serialize_ec2_query(
            value["rules"], pairs, f"{prefix}.RuleSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPrefixListResolverRulesResult:
    out: GetIpamPrefixListResolverRulesResult = {}  # type: ignore[typeddict-item]
    if el.find("RuleSet") is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set

        out["rules"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set.deserialize_ec2_query(
                el, "RuleSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
