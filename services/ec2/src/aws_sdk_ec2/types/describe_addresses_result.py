"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_list


class DescribeAddressesResult(TypedDict, closed=True):
    addresses: NotRequired["aws_sdk_ec2.types.address_list.AddressList"]
    """<p>Information about the Elastic IP addresses.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAddressesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "addresses" in value:
        import aws_sdk_ec2.types.address_list

        aws_sdk_ec2.types.address_list.serialize_ec2_query(
            value["addresses"], pairs, f"{prefix}.AddressesSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeAddressesResult:
    out: DescribeAddressesResult = {}  # type: ignore[typeddict-item]
    if el.find("AddressesSet") is not None:
        import aws_sdk_ec2.types.address_list

        out["addresses"] = aws_sdk_ec2.types.address_list.deserialize_ec2_query(
            el, "AddressesSet"
        )
    return out
