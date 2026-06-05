"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServersList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server

RouteServersList: TypeAlias = list["aws_sdk_ec2.types.route_server.RouteServer"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.route_server

        aws_sdk_ec2.types.route_server.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> RouteServersList:
    import aws_sdk_ec2.types.route_server

    out: RouteServersList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.route_server.deserialize_ec2_query(child))
    return out
