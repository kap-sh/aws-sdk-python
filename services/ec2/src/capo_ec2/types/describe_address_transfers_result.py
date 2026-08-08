"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressTransfersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_transfer_list
    import capo_ec2.types.string


class DescribeAddressTransfersResult(TypedDict, closed=True):
    address_transfers: NotRequired[
        "capo_ec2.types.address_transfer_list.AddressTransferList"
    ]
    """<p>The Elastic IP address transfer.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAddressTransfersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "address_transfers" in value:
        import capo_ec2.types.address_transfer_list

        capo_ec2.types.address_transfer_list.serialize_ec2_query(
            value["address_transfers"], pairs, f"{key_prefix}AddressTransferSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeAddressTransfersResult:
    out: DescribeAddressTransfersResult = {}  # type: ignore[typeddict-item]
    if el.find("addressTransferSet") is not None:
        import capo_ec2.types.address_transfer_list

        out["address_transfers"] = (
            capo_ec2.types.address_transfer_list.deserialize_ec2_query(
                el, "addressTransferSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
