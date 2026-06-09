"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedPrefixListSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_prefix_list

ManagedPrefixListSet: TypeAlias = list[
    "aws_sdk_ec2.types.managed_prefix_list.ManagedPrefixList"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ManagedPrefixListSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.managed_prefix_list

        aws_sdk_ec2.types.managed_prefix_list.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ManagedPrefixListSet:
    import aws_sdk_ec2.types.managed_prefix_list

    out: ManagedPrefixListSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.managed_prefix_list.deserialize_ec2_query(child))
    return out
