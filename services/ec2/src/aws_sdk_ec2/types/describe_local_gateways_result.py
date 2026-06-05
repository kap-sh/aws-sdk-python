"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewaysResult(TypedDict):
    local_gateways: NotRequired["aws_sdk_ec2.types.local_gateway_set.LocalGatewaySet"]
    """<p>Information about the local gateways.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "local_gateways" in value:
        import aws_sdk_ec2.types.local_gateway_set

        aws_sdk_ec2.types.local_gateway_set.serialize_ec2_query(
            value["local_gateways"], pairs, f"{prefix}.LocalGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeLocalGatewaysResult:
    out: DescribeLocalGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewaySet") is not None:
        import aws_sdk_ec2.types.local_gateway_set

        out["local_gateways"] = (
            aws_sdk_ec2.types.local_gateway_set.deserialize_ec2_query(
                el, "LocalGatewaySet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
