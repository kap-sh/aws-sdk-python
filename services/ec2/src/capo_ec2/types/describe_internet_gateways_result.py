"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInternetGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.internet_gateway_list
    import capo_ec2.types.string


class DescribeInternetGatewaysResult(TypedDict, closed=True):
    internet_gateways: NotRequired[
        "capo_ec2.types.internet_gateway_list.InternetGatewayList"
    ]
    """<p>Information about the internet gateways.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInternetGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "internet_gateways" in value:
        import capo_ec2.types.internet_gateway_list

        capo_ec2.types.internet_gateway_list.serialize_ec2_query(
            value["internet_gateways"], pairs, f"{key_prefix}InternetGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInternetGatewaysResult:
    out: DescribeInternetGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("internetGatewaySet") is not None:
        import capo_ec2.types.internet_gateway_list

        out["internet_gateways"] = (
            capo_ec2.types.internet_gateway_list.deserialize_ec2_query(
                el, "internetGatewaySet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
