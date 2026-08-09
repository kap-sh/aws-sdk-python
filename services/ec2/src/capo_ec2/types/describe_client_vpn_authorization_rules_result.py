"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnAuthorizationRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.authorization_rule_set
    import capo_ec2.types.next_token


class DescribeClientVpnAuthorizationRulesResult(TypedDict, closed=True):
    authorization_rules: NotRequired[
        "capo_ec2.types.authorization_rule_set.AuthorizationRuleSet"
    ]
    """<p>Information about the authorization rules.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnAuthorizationRulesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "authorization_rules" in value:
        import capo_ec2.types.authorization_rule_set

        capo_ec2.types.authorization_rule_set.serialize_ec2_query(
            value["authorization_rules"], pairs, f"{key_prefix}AuthorizationRule"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnAuthorizationRulesResult:
    out: DescribeClientVpnAuthorizationRulesResult = {}  # type: ignore[typeddict-item]
    child_authorization_rules = el.find("authorizationRule")
    if child_authorization_rules is not None:
        import capo_ec2.types.authorization_rule_set

        out["authorization_rules"] = (
            capo_ec2.types.authorization_rule_set.deserialize_ec2_query(
                child_authorization_rules
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
