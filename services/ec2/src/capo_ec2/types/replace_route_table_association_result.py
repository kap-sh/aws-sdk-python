"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRouteTableAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_table_association_state
    import capo_ec2.types.string


class ReplaceRouteTableAssociationResult(TypedDict, closed=True):
    new_association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the new association.</p>"""
    association_state: NotRequired[
        "capo_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceRouteTableAssociationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "new_association_id" in value:
        pairs.append((f"{prefix}.NewAssociationId", str(value["new_association_id"])))
    if "association_state" in value:
        import capo_ec2.types.route_table_association_state

        capo_ec2.types.route_table_association_state.serialize_ec2_query(
            value["association_state"], pairs, f"{prefix}.AssociationState"
        )


def deserialize_ec2_query(el: Element) -> ReplaceRouteTableAssociationResult:
    out: ReplaceRouteTableAssociationResult = {}  # type: ignore[typeddict-item]
    child_new_association_id = el.find("NewAssociationId")
    if child_new_association_id is not None:
        out["new_association_id"] = str(child_new_association_id.text or "")
    child_association_state = el.find("AssociationState")
    if child_association_state is not None:
        import capo_ec2.types.route_table_association_state

        out["association_state"] = (
            capo_ec2.types.route_table_association_state.deserialize_ec2_query(
                child_association_state
            )
        )
    return out
