"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table

RouteTableList: TypeAlias = list["aws_sdk_ec2.types.route_table.RouteTable"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteTableList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.route_table

        aws_sdk_ec2.types.route_table.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> RouteTableList:
    import aws_sdk_ec2.types.route_table

    out: RouteTableList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.route_table.deserialize_ec2_query(child))
    return out
