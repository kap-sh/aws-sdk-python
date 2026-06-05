"""Generated from Smithy shape ``com.amazonaws.ec2#CreateEgressOnlyInternetGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway
    import aws_sdk_ec2.types.string


class CreateEgressOnlyInternetGatewayResult(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    egress_only_internet_gateway: NotRequired[
        "aws_sdk_ec2.types.egress_only_internet_gateway.EgressOnlyInternetGateway"
    ]
    """<p>Information about the egress-only internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateEgressOnlyInternetGatewayResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "egress_only_internet_gateway" in value:
        import aws_sdk_ec2.types.egress_only_internet_gateway

        aws_sdk_ec2.types.egress_only_internet_gateway.serialize_ec2_query(
            value["egress_only_internet_gateway"],
            pairs,
            f"{prefix}.EgressOnlyInternetGateway",
        )


def deserialize_ec2_query(el: Element) -> CreateEgressOnlyInternetGatewayResult:
    out: CreateEgressOnlyInternetGatewayResult = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_egress_only_internet_gateway = el.find("EgressOnlyInternetGateway")
    if child_egress_only_internet_gateway is not None:
        import aws_sdk_ec2.types.egress_only_internet_gateway

        out["egress_only_internet_gateway"] = (
            aws_sdk_ec2.types.egress_only_internet_gateway.deserialize_ec2_query(
                child_egress_only_internet_gateway
            )
        )
    return out
