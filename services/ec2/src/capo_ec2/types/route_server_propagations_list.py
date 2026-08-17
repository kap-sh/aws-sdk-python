"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPropagationsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_propagation

RouteServerPropagationsList: TypeAlias = list[
    "capo_ec2.types.route_server_propagation.RouteServerPropagation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerPropagationsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route_server_propagation

        capo_ec2.types.route_server_propagation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RouteServerPropagationsList:
    import capo_ec2.types.route_server_propagation

    out: RouteServerPropagationsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.route_server_propagation.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> RouteServerPropagationsList:
    import capo_ec2.types.route_server_propagation

    out: RouteServerPropagationsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.route_server_propagation.deserialize_ec2_query(child))
    return out
