"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteEgressOnlyInternetGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.egress_only_internet_gateway_id


class DeleteEgressOnlyInternetGatewayRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    egress_only_internet_gateway_id: NotRequired[
        "capo_ec2.types.egress_only_internet_gateway_id.EgressOnlyInternetGatewayId"
    ]
    """<p>The ID of the egress-only internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteEgressOnlyInternetGatewayRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "egress_only_internet_gateway_id" in value:
        pairs.append(
            (
                f"{key_prefix}EgressOnlyInternetGatewayId",
                str(value["egress_only_internet_gateway_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteEgressOnlyInternetGatewayRequest:
    out: DeleteEgressOnlyInternetGatewayRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_egress_only_internet_gateway_id = el.find("EgressOnlyInternetGatewayId")
    if child_egress_only_internet_gateway_id is not None:
        out["egress_only_internet_gateway_id"] = str(
            child_egress_only_internet_gateway_id.text or ""
        )
    return out
