"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_associations_list


class GetRouteServerAssociationsResult(TypedDict, closed=True):
    route_server_associations: NotRequired[
        "capo_ec2.types.route_server_associations_list.RouteServerAssociationsList"
    ]
    """<p>Information about the associations for the specified route server.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerAssociationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_associations" in value:
        import capo_ec2.types.route_server_associations_list

        capo_ec2.types.route_server_associations_list.serialize_ec2_query(
            value["route_server_associations"],
            pairs,
            f"{key_prefix}RouteServerAssociationSet",
        )


def deserialize_ec2_query(el: Element) -> GetRouteServerAssociationsResult:
    out: GetRouteServerAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteServerAssociationSet") is not None:
        import capo_ec2.types.route_server_associations_list

        out["route_server_associations"] = (
            capo_ec2.types.route_server_associations_list.deserialize_ec2_query(
                el, "RouteServerAssociationSet"
            )
        )
    return out
