"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateSecurityGroupVpcResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_vpc_association_state


class AssociateSecurityGroupVpcResult(TypedDict, closed=True):
    state: NotRequired[
        "capo_ec2.types.security_group_vpc_association_state.SecurityGroupVpcAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateSecurityGroupVpcResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import capo_ec2.types.security_group_vpc_association_state

        capo_ec2.types.security_group_vpc_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> AssociateSecurityGroupVpcResult:
    out: AssociateSecurityGroupVpcResult = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.security_group_vpc_association_state

        out["state"] = (
            capo_ec2.types.security_group_vpc_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
