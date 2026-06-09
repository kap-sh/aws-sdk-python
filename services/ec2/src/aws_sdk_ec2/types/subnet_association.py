"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state


class SubnetAssociation(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state.TransitGatewayMulitcastDomainAssociationState"
    ]
    """<p>The state of the subnet association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state

        aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> SubnetAssociation:
    out: SubnetAssociation = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
