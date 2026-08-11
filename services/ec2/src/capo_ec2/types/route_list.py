"""Generated from Smithy shape ``com.amazonaws.ec2#RouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route

RouteList: TypeAlias = list["capo_ec2.types.route.Route"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route

        capo_ec2.types.route.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> RouteList:
    import capo_ec2.types.route

    out: RouteList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.route.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RouteList:
    import capo_ec2.types.route

    out: RouteList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.route.deserialize_ec2_query(child))
    return out
