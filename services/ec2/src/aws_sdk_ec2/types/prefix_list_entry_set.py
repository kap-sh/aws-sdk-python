"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListEntrySet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_entry

PrefixListEntrySet: TypeAlias = list[
    "aws_sdk_ec2.types.prefix_list_entry.PrefixListEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrefixListEntrySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.prefix_list_entry

        aws_sdk_ec2.types.prefix_list_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PrefixListEntrySet:
    import aws_sdk_ec2.types.prefix_list_entry

    out: PrefixListEntrySet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.prefix_list_entry.deserialize_ec2_query(child))
    return out
