"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint


class CreateVpcEndpointResult(TypedDict, closed=True):
    vpc_endpoint: NotRequired["aws_sdk_ec2.types.vpc_endpoint.VpcEndpoint"]
    """<p>Information about the endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_endpoint" in value:
        import aws_sdk_ec2.types.vpc_endpoint

        aws_sdk_ec2.types.vpc_endpoint.serialize_ec2_query(
            value["vpc_endpoint"], pairs, f"{prefix}.VpcEndpoint"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateVpcEndpointResult:
    out: CreateVpcEndpointResult = {}  # type: ignore[typeddict-item]
    child_vpc_endpoint = el.find("VpcEndpoint")
    if child_vpc_endpoint is not None:
        import aws_sdk_ec2.types.vpc_endpoint

        out["vpc_endpoint"] = aws_sdk_ec2.types.vpc_endpoint.deserialize_ec2_query(
            child_vpc_endpoint
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
