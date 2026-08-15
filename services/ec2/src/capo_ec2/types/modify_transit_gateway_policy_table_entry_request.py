"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayPolicyTableEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_policy_table_id
    import capo_ec2.types.transit_gateway_request_policy_rule
    import capo_ec2.types.transit_gateway_route_table_id


class ModifyTransitGatewayPolicyTableEntryRequest(TypedDict, closed=True):
    transit_gateway_policy_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_policy_table_id.TransitGatewayPolicyTableId"
    ]
    """<p>The ID of the transit gateway policy table.</p>"""
    policy_rule_number: NotRequired["capo_ec2.types.string.String"]
    """<p>The rule number of the policy table entry to modify.</p>"""
    policy_rule: NotRequired[
        "capo_ec2.types.transit_gateway_request_policy_rule.TransitGatewayRequestPolicyRule"
    ]
    """<p>The updated matching criteria for the policy table entry. Unspecified fields retain their current values.</p>"""
    target_route_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the transit gateway route table to use for traffic matching this rule.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayPolicyTableEntryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_policy_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayPolicyTableId",
                str(value["transit_gateway_policy_table_id"]),
            )
        )
    if "policy_rule_number" in value:
        pairs.append(
            (f"{key_prefix}PolicyRuleNumber", str(value["policy_rule_number"]))
        )
    if "policy_rule" in value:
        import capo_ec2.types.transit_gateway_request_policy_rule

        capo_ec2.types.transit_gateway_request_policy_rule.serialize_ec2_query(
            value["policy_rule"], pairs, f"{key_prefix}PolicyRule"
        )
    if "target_route_table_id" in value:
        pairs.append(
            (f"{key_prefix}TargetRouteTableId", str(value["target_route_table_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayPolicyTableEntryRequest:
    out: ModifyTransitGatewayPolicyTableEntryRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_policy_table_id = el.find("TransitGatewayPolicyTableId")
    if child_transit_gateway_policy_table_id is not None:
        out["transit_gateway_policy_table_id"] = str(
            child_transit_gateway_policy_table_id.text or ""
        )
    child_policy_rule_number = el.find("PolicyRuleNumber")
    if child_policy_rule_number is not None:
        out["policy_rule_number"] = str(child_policy_rule_number.text or "")
    child_policy_rule = el.find("PolicyRule")
    if child_policy_rule is not None:
        import capo_ec2.types.transit_gateway_request_policy_rule

        out["policy_rule"] = (
            capo_ec2.types.transit_gateway_request_policy_rule.deserialize_ec2_query(
                child_policy_rule
            )
        )
    child_target_route_table_id = el.find("TargetRouteTableId")
    if child_target_route_table_id is not None:
        out["target_route_table_id"] = str(child_target_route_table_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
