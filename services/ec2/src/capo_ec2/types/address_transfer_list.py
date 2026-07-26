"""Generated from Smithy shape ``com.amazonaws.ec2#AddressTransferList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_transfer

AddressTransferList: TypeAlias = list["capo_ec2.types.address_transfer.AddressTransfer"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddressTransferList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.address_transfer

        capo_ec2.types.address_transfer.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AddressTransferList:
    import capo_ec2.types.address_transfer

    out: AddressTransferList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.address_transfer.deserialize_ec2_query(child))
    return out
