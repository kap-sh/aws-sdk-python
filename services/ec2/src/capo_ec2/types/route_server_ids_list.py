"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_id

RouteServerIdsList: TypeAlias = list["capo_ec2.types.route_server_id.RouteServerId"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> RouteServerIdsList:
    out: RouteServerIdsList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RouteServerIdsList:
    out: RouteServerIdsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
