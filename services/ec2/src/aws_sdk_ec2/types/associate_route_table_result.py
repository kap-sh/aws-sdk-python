"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_association_state
    import aws_sdk_ec2.types.string


class AssociateRouteTableResult(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The route table association ID. This ID is required for disassociating the route table.</p>"""
    association_state: NotRequired[
        "aws_sdk_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateRouteTableResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "association_state" in value:
        import aws_sdk_ec2.types.route_table_association_state

        aws_sdk_ec2.types.route_table_association_state.serialize_ec2_query(
            value["association_state"], pairs, f"{prefix}.AssociationState"
        )


def deserialize_ec2_query(el: Element) -> AssociateRouteTableResult:
    out: AssociateRouteTableResult = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_association_state = el.find("AssociationState")
    if child_association_state is not None:
        import aws_sdk_ec2.types.route_table_association_state

        out["association_state"] = (
            aws_sdk_ec2.types.route_table_association_state.deserialize_ec2_query(
                child_association_state
            )
        )
    return out
