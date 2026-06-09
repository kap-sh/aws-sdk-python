"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAddressTransferResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_transfer


class DisableAddressTransferResult(TypedDict):
    address_transfer: NotRequired["aws_sdk_ec2.types.address_transfer.AddressTransfer"]
    """<p>An Elastic IP address transfer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableAddressTransferResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "address_transfer" in value:
        import aws_sdk_ec2.types.address_transfer

        aws_sdk_ec2.types.address_transfer.serialize_ec2_query(
            value["address_transfer"], pairs, f"{prefix}.AddressTransfer"
        )


def deserialize_ec2_query(el: Element) -> DisableAddressTransferResult:
    out: DisableAddressTransferResult = {}  # type: ignore[typeddict-item]
    child_address_transfer = el.find("AddressTransfer")
    if child_address_transfer is not None:
        import aws_sdk_ec2.types.address_transfer

        out["address_transfer"] = (
            aws_sdk_ec2.types.address_transfer.deserialize_ec2_query(
                child_address_transfer
            )
        )
    return out
