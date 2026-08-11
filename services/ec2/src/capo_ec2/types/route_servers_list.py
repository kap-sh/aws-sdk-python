"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServersList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server

RouteServersList: TypeAlias = list["capo_ec2.types.route_server.RouteServer"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route_server

        capo_ec2.types.route_server.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> RouteServersList:
    import capo_ec2.types.route_server

    out: RouteServersList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.route_server.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RouteServersList:
    import capo_ec2.types.route_server

    out: RouteServersList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.route_server.deserialize_ec2_query(child))
    return out
