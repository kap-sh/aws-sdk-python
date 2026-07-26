"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateNatGatewayAddressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.nat_gateway_address_list
    import capo_ec2.types.nat_gateway_id


class AssignPrivateNatGatewayAddressResult(TypedDict, closed=True):
    nat_gateway_id: NotRequired["capo_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    nat_gateway_addresses: NotRequired[
        "capo_ec2.types.nat_gateway_address_list.NatGatewayAddressList"
    ]
    """<p>NAT gateway IP addresses.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignPrivateNatGatewayAddressResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))
    if "nat_gateway_addresses" in value:
        import capo_ec2.types.nat_gateway_address_list

        capo_ec2.types.nat_gateway_address_list.serialize_ec2_query(
            value["nat_gateway_addresses"], pairs, f"{prefix}.NatGatewayAddressSet"
        )


def deserialize_ec2_query(el: Element) -> AssignPrivateNatGatewayAddressResult:
    out: AssignPrivateNatGatewayAddressResult = {}  # type: ignore[typeddict-item]
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    if el.find("NatGatewayAddressSet") is not None:
        import capo_ec2.types.nat_gateway_address_list

        out["nat_gateway_addresses"] = (
            capo_ec2.types.nat_gateway_address_list.deserialize_ec2_query(
                el, "NatGatewayAddressSet"
            )
        )
    return out
