"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_association

RouteServerAssociationsList: TypeAlias = list[
    "capo_ec2.types.route_server_association.RouteServerAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerAssociationsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route_server_association

        capo_ec2.types.route_server_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RouteServerAssociationsList:
    import capo_ec2.types.route_server_association

    out: RouteServerAssociationsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.route_server_association.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> RouteServerAssociationsList:
    import capo_ec2.types.route_server_association

    out: RouteServerAssociationsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.route_server_association.deserialize_ec2_query(child))
    return out
