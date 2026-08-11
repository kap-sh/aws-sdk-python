"""Generated from Smithy shape ``com.amazonaws.ec2#TargetNetworkSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.target_network

TargetNetworkSet: TypeAlias = list["capo_ec2.types.target_network.TargetNetwork"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetNetworkSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.target_network

        capo_ec2.types.target_network.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> TargetNetworkSet:
    import capo_ec2.types.target_network

    out: TargetNetworkSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.target_network.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TargetNetworkSet:
    import capo_ec2.types.target_network

    out: TargetNetworkSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.target_network.deserialize_ec2_query(child))
    return out
