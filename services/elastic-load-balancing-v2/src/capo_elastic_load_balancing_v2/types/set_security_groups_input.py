"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetSecurityGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum
    import capo_elastic_load_balancing_v2.types.load_balancer_arn
    import capo_elastic_load_balancing_v2.types.security_groups


class SetSecurityGroupsInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    security_groups: NotRequired[
        "capo_elastic_load_balancing_v2.types.security_groups.SecurityGroups"
    ]
    """<p>The IDs of the security groups.</p>"""
    enforce_security_group_inbound_rules_on_private_link_traffic: NotRequired[
        "capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum.EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum"
    ]
    """<p>Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through Amazon Web Services PrivateLink. Applies only if the load balancer has an associated security group. The default is <code>on</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSecurityGroupsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "security_groups" in value:
        import capo_elastic_load_balancing_v2.types.security_groups

        capo_elastic_load_balancing_v2.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
        )
    if "enforce_security_group_inbound_rules_on_private_link_traffic" in value:
        import capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum

        capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum.serialize_query(
            value["enforce_security_group_inbound_rules_on_private_link_traffic"],
            pairs,
            f"{key_prefix}EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic",
        )


def deserialize_query(el: Element) -> SetSecurityGroupsInput:
    out: SetSecurityGroupsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_elastic_load_balancing_v2.types.security_groups

        out["security_groups"] = (
            capo_elastic_load_balancing_v2.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    child_enforce_security_group_inbound_rules_on_private_link_traffic = el.find(
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic"
    )
    if child_enforce_security_group_inbound_rules_on_private_link_traffic is not None:
        import capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum

        out["enforce_security_group_inbound_rules_on_private_link_traffic"] = (
            capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum.deserialize_query(
                child_enforce_security_group_inbound_rules_on_private_link_traffic
            )
        )
    return out
