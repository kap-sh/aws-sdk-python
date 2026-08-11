"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_endpoint

RouteServerEndpointsList: TypeAlias = list[
    "capo_ec2.types.route_server_endpoint.RouteServerEndpoint"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerEndpointsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route_server_endpoint

        capo_ec2.types.route_server_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RouteServerEndpointsList:
    import capo_ec2.types.route_server_endpoint

    out: RouteServerEndpointsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.route_server_endpoint.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RouteServerEndpointsList:
    import capo_ec2.types.route_server_endpoint

    out: RouteServerEndpointsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.route_server_endpoint.deserialize_ec2_query(child))
    return out
