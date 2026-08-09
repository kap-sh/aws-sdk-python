"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteInstallationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_route_installation_detail

RouteServerRouteInstallationDetails: TypeAlias = list[
    "capo_ec2.types.route_server_route_installation_detail.RouteServerRouteInstallationDetail"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerRouteInstallationDetails,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route_server_route_installation_detail

        capo_ec2.types.route_server_route_installation_detail.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RouteServerRouteInstallationDetails:
    import capo_ec2.types.route_server_route_installation_detail

    out: RouteServerRouteInstallationDetails = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.route_server_route_installation_detail.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> RouteServerRouteInstallationDetails:
    import capo_ec2.types.route_server_route_installation_detail

    out: RouteServerRouteInstallationDetails = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.route_server_route_installation_detail.deserialize_ec2_query(
                child
            )
        )
    return out
