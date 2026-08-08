"""Generated from Smithy shape ``com.amazonaws.ec2#CreateEgressOnlyInternetGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.egress_only_internet_gateway
    import capo_ec2.types.string


class CreateEgressOnlyInternetGatewayResult(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    egress_only_internet_gateway: NotRequired[
        "capo_ec2.types.egress_only_internet_gateway.EgressOnlyInternetGateway"
    ]
    """<p>Information about the egress-only internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateEgressOnlyInternetGatewayResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "egress_only_internet_gateway" in value:
        import capo_ec2.types.egress_only_internet_gateway

        capo_ec2.types.egress_only_internet_gateway.serialize_ec2_query(
            value["egress_only_internet_gateway"],
            pairs,
            f"{key_prefix}EgressOnlyInternetGateway",
        )


def deserialize_ec2_query(el: Element) -> CreateEgressOnlyInternetGatewayResult:
    out: CreateEgressOnlyInternetGatewayResult = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_egress_only_internet_gateway = el.find("egressOnlyInternetGateway")
    if child_egress_only_internet_gateway is not None:
        import capo_ec2.types.egress_only_internet_gateway

        out["egress_only_internet_gateway"] = (
            capo_ec2.types.egress_only_internet_gateway.deserialize_ec2_query(
                child_egress_only_internet_gateway
            )
        )
    return out
