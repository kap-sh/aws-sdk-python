"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_set
    import capo_ec2.types.string


class DescribeLocalGatewaysResult(TypedDict, closed=True):
    local_gateways: NotRequired["capo_ec2.types.local_gateway_set.LocalGatewaySet"]
    """<p>Information about the local gateways.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateways" in value:
        import capo_ec2.types.local_gateway_set

        capo_ec2.types.local_gateway_set.serialize_ec2_query(
            value["local_gateways"], pairs, f"{key_prefix}LocalGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeLocalGatewaysResult:
    out: DescribeLocalGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("localGatewaySet") is not None:
        import capo_ec2.types.local_gateway_set

        out["local_gateways"] = capo_ec2.types.local_gateway_set.deserialize_ec2_query(
            el, "localGatewaySet"
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
