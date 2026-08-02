"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_connect


class CreateTransitGatewayConnectResult(TypedDict, closed=True):
    transit_gateway_connect: NotRequired[
        "capo_ec2.types.transit_gateway_connect.TransitGatewayConnect"
    ]
    """<p>Information about the Connect attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayConnectResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_connect" in value:
        import capo_ec2.types.transit_gateway_connect

        capo_ec2.types.transit_gateway_connect.serialize_ec2_query(
            value["transit_gateway_connect"],
            pairs,
            f"{key_prefix}TransitGatewayConnect",
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayConnectResult:
    out: CreateTransitGatewayConnectResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_connect = el.find("TransitGatewayConnect")
    if child_transit_gateway_connect is not None:
        import capo_ec2.types.transit_gateway_connect

        out["transit_gateway_connect"] = (
            capo_ec2.types.transit_gateway_connect.deserialize_ec2_query(
                child_transit_gateway_connect
            )
        )
    return out
