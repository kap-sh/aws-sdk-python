"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNatGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway
    import aws_sdk_ec2.types.string


class CreateNatGatewayResult(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
    nat_gateway: NotRequired["aws_sdk_ec2.types.nat_gateway.NatGateway"]
    """<p>Information about the NAT gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNatGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "nat_gateway" in value:
        import aws_sdk_ec2.types.nat_gateway

        aws_sdk_ec2.types.nat_gateway.serialize_ec2_query(
            value["nat_gateway"], pairs, f"{prefix}.NatGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateNatGatewayResult:
    out: CreateNatGatewayResult = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_nat_gateway = el.find("NatGateway")
    if child_nat_gateway is not None:
        import aws_sdk_ec2.types.nat_gateway

        out["nat_gateway"] = aws_sdk_ec2.types.nat_gateway.deserialize_ec2_query(
            child_nat_gateway
        )
    return out
