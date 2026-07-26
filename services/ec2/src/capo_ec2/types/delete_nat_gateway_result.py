"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNatGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class DeleteNatGatewayResult(TypedDict, closed=True):
    nat_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the NAT gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNatGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))


def deserialize_ec2_query(el: Element) -> DeleteNatGatewayResult:
    out: DeleteNatGatewayResult = {}  # type: ignore[typeddict-item]
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    return out
