"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayPolicyTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.transit_gateway_policy_table_id


class DeleteTransitGatewayPolicyTableRequest(TypedDict, closed=True):
    transit_gateway_policy_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_id.TransitGatewayPolicyTableId"
    ]
    """<p>The transit gateway policy table to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayPolicyTableRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_policy_table_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayPolicyTableId",
                str(value["transit_gateway_policy_table_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayPolicyTableRequest:
    out: DeleteTransitGatewayPolicyTableRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_policy_table_id = el.find("TransitGatewayPolicyTableId")
    if child_transit_gateway_policy_table_id is not None:
        out["transit_gateway_policy_table_id"] = str(
            child_transit_gateway_policy_table_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
