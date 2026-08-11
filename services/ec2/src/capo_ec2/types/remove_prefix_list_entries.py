"""Generated from Smithy shape ``com.amazonaws.ec2#RemovePrefixListEntries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.remove_prefix_list_entry

RemovePrefixListEntries: TypeAlias = list[
    "capo_ec2.types.remove_prefix_list_entry.RemovePrefixListEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RemovePrefixListEntries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.remove_prefix_list_entry

        capo_ec2.types.remove_prefix_list_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RemovePrefixListEntries:
    import capo_ec2.types.remove_prefix_list_entry

    out: RemovePrefixListEntries = []
    for child in el.findall("member"):
        out.append(capo_ec2.types.remove_prefix_list_entry.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RemovePrefixListEntries:
    import capo_ec2.types.remove_prefix_list_entry

    out: RemovePrefixListEntries = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.remove_prefix_list_entry.deserialize_ec2_query(child))
    return out
