"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetSecurityGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum
    import capo_elastic_load_balancing_v2.types.security_groups


class SetSecurityGroupsOutput(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_elastic_load_balancing_v2.types.security_groups.SecurityGroups"
    ]
    """<p>The IDs of the security groups associated with the load balancer.</p>"""
    enforce_security_group_inbound_rules_on_private_link_traffic: NotRequired[
        "capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum.EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum"
    ]
    """<p>Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through Amazon Web Services PrivateLink.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSecurityGroupsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "security_group_ids" in value:
        import capo_elastic_load_balancing_v2.types.security_groups

        capo_elastic_load_balancing_v2.types.security_groups.serialize_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupIds"
        )
    if "enforce_security_group_inbound_rules_on_private_link_traffic" in value:
        import capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum

        capo_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic_enum.serialize_query(
            value["enforce_security_group_inbound_rules_on_private_link_traffic"],
            pairs,
            f"{key_prefix}EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic",
        )


def deserialize_query(el: Element) -> SetSecurityGroupsOutput:
    out: SetSecurityGroupsOutput = {}  # type: ignore[typeddict-item]
    child_security_group_ids = el.find("SecurityGroupIds")
    if child_security_group_ids is not None:
        import capo_elastic_load_balancing_v2.types.security_groups

        out["security_group_ids"] = (
            capo_elastic_load_balancing_v2.types.security_groups.deserialize_query(
                child_security_group_ids
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
