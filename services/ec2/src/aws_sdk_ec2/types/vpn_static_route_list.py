"""Generated from Smithy shape ``com.amazonaws.ec2#VpnStaticRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_static_route

VpnStaticRouteList: TypeAlias = list[
    "aws_sdk_ec2.types.vpn_static_route.VpnStaticRoute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnStaticRouteList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vpn_static_route

        aws_sdk_ec2.types.vpn_static_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VpnStaticRouteList:
    import aws_sdk_ec2.types.vpn_static_route

    out: VpnStaticRouteList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.vpn_static_route.deserialize_ec2_query(child))
    return out
