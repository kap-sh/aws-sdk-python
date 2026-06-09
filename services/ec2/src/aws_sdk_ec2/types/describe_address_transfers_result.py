"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressTransfersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_transfer_list
    import aws_sdk_ec2.types.string


class DescribeAddressTransfersResult(TypedDict):
    address_transfers: NotRequired[
        "aws_sdk_ec2.types.address_transfer_list.AddressTransferList"
    ]
    """<p>The Elastic IP address transfer.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAddressTransfersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "address_transfers" in value:
        import aws_sdk_ec2.types.address_transfer_list

        aws_sdk_ec2.types.address_transfer_list.serialize_ec2_query(
            value["address_transfers"], pairs, f"{prefix}.AddressTransferSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeAddressTransfersResult:
    out: DescribeAddressTransfersResult = {}  # type: ignore[typeddict-item]
    if el.find("AddressTransferSet") is not None:
        import aws_sdk_ec2.types.address_transfer_list

        out["address_transfers"] = (
            aws_sdk_ec2.types.address_transfer_list.deserialize_ec2_query(
                el, "AddressTransferSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
