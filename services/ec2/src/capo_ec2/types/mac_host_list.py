"""Generated from Smithy shape ``com.amazonaws.ec2#MacHostList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.mac_host

MacHostList: TypeAlias = list["capo_ec2.types.mac_host.MacHost"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacHostList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.mac_host

        capo_ec2.types.mac_host.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> MacHostList:
    import capo_ec2.types.mac_host

    out: MacHostList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.mac_host.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> MacHostList:
    import capo_ec2.types.mac_host

    out: MacHostList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.mac_host.deserialize_ec2_query(child))
    return out
