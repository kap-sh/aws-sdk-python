"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAddressTransferResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_transfer


class DisableAddressTransferResult(TypedDict, closed=True):
    address_transfer: NotRequired["capo_ec2.types.address_transfer.AddressTransfer"]
    """<p>An Elastic IP address transfer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableAddressTransferResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "address_transfer" in value:
        import capo_ec2.types.address_transfer

        capo_ec2.types.address_transfer.serialize_ec2_query(
            value["address_transfer"], pairs, f"{key_prefix}AddressTransfer"
        )


def deserialize_ec2_query(el: Element) -> DisableAddressTransferResult:
    out: DisableAddressTransferResult = {}  # type: ignore[typeddict-item]
    child_address_transfer = el.find("addressTransfer")
    if child_address_transfer is not None:
        import capo_ec2.types.address_transfer

        out["address_transfer"] = capo_ec2.types.address_transfer.deserialize_ec2_query(
            child_address_transfer
        )
    return out
