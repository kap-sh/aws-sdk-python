"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_policy_rule
    import capo_ec2.types.transit_gateway_route_table_id


class TransitGatewayPolicyTableEntry(TypedDict, closed=True):
    policy_rule_number: NotRequired["capo_ec2.types.string.String"]
    """<p>The rule number for the transit gateway policy table entry.</p>"""
    policy_rule: NotRequired[
        "capo_ec2.types.transit_gateway_policy_rule.TransitGatewayPolicyRule"
    ]
    """<p>The policy rule associated with the transit gateway policy table.</p>"""
    target_route_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the target route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_rule_number" in value:
        pairs.append(
            (f"{key_prefix}PolicyRuleNumber", str(value["policy_rule_number"]))
        )
    if "policy_rule" in value:
        import capo_ec2.types.transit_gateway_policy_rule

        capo_ec2.types.transit_gateway_policy_rule.serialize_ec2_query(
            value["policy_rule"], pairs, f"{key_prefix}PolicyRule"
        )
    if "target_route_table_id" in value:
        pairs.append(
            (f"{key_prefix}TargetRouteTableId", str(value["target_route_table_id"]))
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableEntry:
    out: TransitGatewayPolicyTableEntry = {}  # type: ignore[typeddict-item]
    child_policy_rule_number = el.find("PolicyRuleNumber")
    if child_policy_rule_number is not None:
        out["policy_rule_number"] = str(child_policy_rule_number.text or "")
    child_policy_rule = el.find("PolicyRule")
    if child_policy_rule is not None:
        import capo_ec2.types.transit_gateway_policy_rule

        out["policy_rule"] = (
            capo_ec2.types.transit_gateway_policy_rule.deserialize_ec2_query(
                child_policy_rule
            )
        )
    child_target_route_table_id = el.find("TargetRouteTableId")
    if child_target_route_table_id is not None:
        out["target_route_table_id"] = str(child_target_route_table_id.text or "")
    return out
