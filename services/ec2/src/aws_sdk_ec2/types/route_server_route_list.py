"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_route

RouteServerRouteList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_route.RouteServerRoute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerRouteList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.route_server_route

        aws_sdk_ec2.types.route_server_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RouteServerRouteList:
    import aws_sdk_ec2.types.route_server_route

    out: RouteServerRouteList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.route_server_route.deserialize_ec2_query(child))
    return out
