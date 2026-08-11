"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_subnet

SecondarySubnetList: TypeAlias = list["capo_ec2.types.secondary_subnet.SecondarySubnet"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondarySubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.secondary_subnet

        capo_ec2.types.secondary_subnet.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SecondarySubnetList:
    import capo_ec2.types.secondary_subnet

    out: SecondarySubnetList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.secondary_subnet.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SecondarySubnetList:
    import capo_ec2.types.secondary_subnet

    out: SecondarySubnetList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.secondary_subnet.deserialize_ec2_query(child))
    return out
