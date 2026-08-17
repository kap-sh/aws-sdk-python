"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPairList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.key_pair_info

KeyPairList: TypeAlias = list["capo_ec2.types.key_pair_info.KeyPairInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: KeyPairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.key_pair_info

        capo_ec2.types.key_pair_info.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> KeyPairList:
    import capo_ec2.types.key_pair_info

    out: KeyPairList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.key_pair_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> KeyPairList:
    import capo_ec2.types.key_pair_info

    out: KeyPairList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.key_pair_info.deserialize_ec2_query(child))
    return out
