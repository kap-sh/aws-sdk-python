"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_table_association_state
    import capo_ec2.types.string


class AssociateRouteTableResult(TypedDict, closed=True):
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The route table association ID. This ID is required for disassociating the route table.</p>"""
    association_state: NotRequired[
        "capo_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateRouteTableResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))
    if "association_state" in value:
        import capo_ec2.types.route_table_association_state

        capo_ec2.types.route_table_association_state.serialize_ec2_query(
            value["association_state"], pairs, f"{key_prefix}AssociationState"
        )


def deserialize_ec2_query(el: Element) -> AssociateRouteTableResult:
    out: AssociateRouteTableResult = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("associationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_association_state = el.find("associationState")
    if child_association_state is not None:
        import capo_ec2.types.route_table_association_state

        out["association_state"] = (
            capo_ec2.types.route_table_association_state.deserialize_ec2_query(
                child_association_state
            )
        )
    return out
