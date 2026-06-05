"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMeteringPolicyEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id


class DeleteTransitGatewayMeteringPolicyEntryRequest(TypedDict):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy containing the entry to delete.</p>"""
    policy_rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number of the metering policy entry to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayMeteringPolicyEntryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_metering_policy_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMeteringPolicyId",
                str(value["transit_gateway_metering_policy_id"]),
            )
        )
    if "policy_rule_number" in value:
        pairs.append((f"{prefix}.PolicyRuleNumber", str(value["policy_rule_number"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DeleteTransitGatewayMeteringPolicyEntryRequest:
    out: DeleteTransitGatewayMeteringPolicyEntryRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_id = el.find("TransitGatewayMeteringPolicyId")
    if child_transit_gateway_metering_policy_id is not None:
        out["transit_gateway_metering_policy_id"] = str(
            child_transit_gateway_metering_policy_id.text or ""
        )
    child_policy_rule_number = el.find("PolicyRuleNumber")
    if child_policy_rule_number is not None:
        out["policy_rule_number"] = int(child_policy_rule_number.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
