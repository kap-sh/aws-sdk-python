"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_acl_entry

NetworkAclEntryList: TypeAlias = list[
    "capo_ec2.types.network_acl_entry.NetworkAclEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAclEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.network_acl_entry

        capo_ec2.types.network_acl_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> NetworkAclEntryList:
    import capo_ec2.types.network_acl_entry

    out: NetworkAclEntryList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.network_acl_entry.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> NetworkAclEntryList:
    import capo_ec2.types.network_acl_entry

    out: NetworkAclEntryList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.network_acl_entry.deserialize_ec2_query(child))
    return out
