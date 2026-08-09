"""Generated from Smithy shape ``com.amazonaws.ec2#AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address

AddressList: TypeAlias = list["capo_ec2.types.address.Address"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.address

        capo_ec2.types.address.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> AddressList:
    import capo_ec2.types.address

    out: AddressList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.address.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AddressList:
    import capo_ec2.types.address

    out: AddressList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.address.deserialize_ec2_query(child))
    return out
