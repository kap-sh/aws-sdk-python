"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateRouteServerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_association


class AssociateRouteServerResult(TypedDict, closed=True):
    route_server_association: NotRequired[
        "capo_ec2.types.route_server_association.RouteServerAssociation"
    ]
    """<p>Information about the association between the route server and the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateRouteServerResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_association" in value:
        import capo_ec2.types.route_server_association

        capo_ec2.types.route_server_association.serialize_ec2_query(
            value["route_server_association"],
            pairs,
            f"{key_prefix}RouteServerAssociation",
        )


def deserialize_ec2_query(el: Element) -> AssociateRouteServerResult:
    out: AssociateRouteServerResult = {}  # type: ignore[typeddict-item]
    child_route_server_association = el.find("RouteServerAssociation")
    if child_route_server_association is not None:
        import capo_ec2.types.route_server_association

        out["route_server_association"] = (
            capo_ec2.types.route_server_association.deserialize_ec2_query(
                child_route_server_association
            )
        )
    return out
