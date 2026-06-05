"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_set
    import aws_sdk_ec2.types.next_token


class DescribeAddressesAttributeResult(TypedDict):
    addresses: NotRequired["aws_sdk_ec2.types.address_set.AddressSet"]
    """<p>Information about the IP addresses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAddressesAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "addresses" in value:
        import aws_sdk_ec2.types.address_set

        aws_sdk_ec2.types.address_set.serialize_ec2_query(
            value["addresses"], pairs, f"{prefix}.AddressSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeAddressesAttributeResult:
    out: DescribeAddressesAttributeResult = {}  # type: ignore[typeddict-item]
    if el.find("AddressSet") is not None:
        import aws_sdk_ec2.types.address_set

        out["addresses"] = aws_sdk_ec2.types.address_set.deserialize_ec2_query(
            el, "AddressSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
