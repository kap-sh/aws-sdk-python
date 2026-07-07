"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table


class DeleteLocalGatewayRouteTableResult(TypedDict, closed=True):
    local_gateway_route_table: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table.LocalGatewayRouteTable"
    ]
    """<p>Information about the local gateway route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayRouteTableResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "local_gateway_route_table" in value:
        import aws_sdk_ec2.types.local_gateway_route_table

        aws_sdk_ec2.types.local_gateway_route_table.serialize_ec2_query(
            value["local_gateway_route_table"],
            pairs,
            f"{prefix}.LocalGatewayRouteTable",
        )


def deserialize_ec2_query(el: Element) -> DeleteLocalGatewayRouteTableResult:
    out: DeleteLocalGatewayRouteTableResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table = el.find("LocalGatewayRouteTable")
    if child_local_gateway_route_table is not None:
        import aws_sdk_ec2.types.local_gateway_route_table

        out["local_gateway_route_table"] = (
            aws_sdk_ec2.types.local_gateway_route_table.deserialize_ec2_query(
                child_local_gateway_route_table
            )
        )
    return out
