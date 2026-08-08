"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_set
    import capo_ec2.types.next_token


class GetIpamPrefixListResolverRulesResult(TypedDict, closed=True):
    rules: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_rule_set.IpamPrefixListResolverRuleSet"
    ]
    """<p>The CIDR selection rules for the IPAM prefix list resolver.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPrefixListResolverRulesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rules" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_set

        capo_ec2.types.ipam_prefix_list_resolver_rule_set.serialize_ec2_query(
            value["rules"], pairs, f"{key_prefix}RuleSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPrefixListResolverRulesResult:
    out: GetIpamPrefixListResolverRulesResult = {}  # type: ignore[typeddict-item]
    if el.find("ruleSet") is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_set

        out["rules"] = (
            capo_ec2.types.ipam_prefix_list_resolver_rule_set.deserialize_ec2_query(
                el, "ruleSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
