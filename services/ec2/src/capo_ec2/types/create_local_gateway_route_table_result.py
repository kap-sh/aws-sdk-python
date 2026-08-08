"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table


class CreateLocalGatewayRouteTableResult(TypedDict, closed=True):
    local_gateway_route_table: NotRequired[
        "capo_ec2.types.local_gateway_route_table.LocalGatewayRouteTable"
    ]
    """<p>Information about the local gateway route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLocalGatewayRouteTableResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table" in value:
        import capo_ec2.types.local_gateway_route_table

        capo_ec2.types.local_gateway_route_table.serialize_ec2_query(
            value["local_gateway_route_table"],
            pairs,
            f"{key_prefix}LocalGatewayRouteTable",
        )


def deserialize_ec2_query(el: Element) -> CreateLocalGatewayRouteTableResult:
    out: CreateLocalGatewayRouteTableResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table = el.find("localGatewayRouteTable")
    if child_local_gateway_route_table is not None:
        import capo_ec2.types.local_gateway_route_table

        out["local_gateway_route_table"] = (
            capo_ec2.types.local_gateway_route_table.deserialize_ec2_query(
                child_local_gateway_route_table
            )
        )
    return out
