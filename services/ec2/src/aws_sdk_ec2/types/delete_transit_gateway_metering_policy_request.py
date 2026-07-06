"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMeteringPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id


class DeleteTransitGatewayMeteringPolicyRequest(TypedDict, closed=True):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayMeteringPolicyRequest,
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
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayMeteringPolicyRequest:
    out: DeleteTransitGatewayMeteringPolicyRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_id = el.find("TransitGatewayMeteringPolicyId")
    if child_transit_gateway_metering_policy_id is not None:
        out["transit_gateway_metering_policy_id"] = str(
            child_transit_gateway_metering_policy_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
