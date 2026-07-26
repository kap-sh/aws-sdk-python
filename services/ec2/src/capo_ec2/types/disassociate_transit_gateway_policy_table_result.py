"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_policy_table_association


class DisassociateTransitGatewayPolicyTableResult(TypedDict, closed=True):
    association: NotRequired[
        "capo_ec2.types.transit_gateway_policy_table_association.TransitGatewayPolicyTableAssociation"
    ]
    """<p>Returns details about the transit gateway policy table disassociation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateTransitGatewayPolicyTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association" in value:
        import capo_ec2.types.transit_gateway_policy_table_association

        capo_ec2.types.transit_gateway_policy_table_association.serialize_ec2_query(
            value["association"], pairs, f"{prefix}.Association"
        )


def deserialize_ec2_query(el: Element) -> DisassociateTransitGatewayPolicyTableResult:
    out: DisassociateTransitGatewayPolicyTableResult = {}  # type: ignore[typeddict-item]
    child_association = el.find("Association")
    if child_association is not None:
        import capo_ec2.types.transit_gateway_policy_table_association

        out["association"] = (
            capo_ec2.types.transit_gateway_policy_table_association.deserialize_ec2_query(
                child_association
            )
        )
    return out
