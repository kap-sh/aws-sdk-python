"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoint

RouteServerEndpointsList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_endpoint.RouteServerEndpoint"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerEndpointsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.route_server_endpoint

        aws_sdk_ec2.types.route_server_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RouteServerEndpointsList:
    import aws_sdk_ec2.types.route_server_endpoint

    out: RouteServerEndpointsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.route_server_endpoint.deserialize_ec2_query(child))
    return out
