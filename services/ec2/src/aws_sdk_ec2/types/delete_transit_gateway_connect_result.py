"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayConnectResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect


class DeleteTransitGatewayConnectResult(TypedDict, closed=True):
    transit_gateway_connect: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect.TransitGatewayConnect"
    ]
    """<p>Information about the deleted Connect attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayConnectResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_connect" in value:
        import aws_sdk_ec2.types.transit_gateway_connect

        aws_sdk_ec2.types.transit_gateway_connect.serialize_ec2_query(
            value["transit_gateway_connect"], pairs, f"{prefix}.TransitGatewayConnect"
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayConnectResult:
    out: DeleteTransitGatewayConnectResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_connect = el.find("TransitGatewayConnect")
    if child_transit_gateway_connect is not None:
        import aws_sdk_ec2.types.transit_gateway_connect

        out["transit_gateway_connect"] = (
            aws_sdk_ec2.types.transit_gateway_connect.deserialize_ec2_query(
                child_transit_gateway_connect
            )
        )
    return out
