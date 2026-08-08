"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_mulitcast_domain_association_state


class SubnetAssociation(TypedDict, closed=True):
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_mulitcast_domain_association_state.TransitGatewayMulitcastDomainAssociationState"
    ]
    """<p>The state of the subnet association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "state" in value:
        import capo_ec2.types.transit_gateway_mulitcast_domain_association_state

        capo_ec2.types.transit_gateway_mulitcast_domain_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> SubnetAssociation:
    out: SubnetAssociation = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_mulitcast_domain_association_state

        out["state"] = (
            capo_ec2.types.transit_gateway_mulitcast_domain_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
