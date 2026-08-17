"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpointIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_endpoint_id

RouteServerEndpointIdsList: TypeAlias = list[
    "capo_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerEndpointIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> RouteServerEndpointIdsList:
    out: RouteServerEndpointIdsList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RouteServerEndpointIdsList:
    out: RouteServerEndpointIdsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
