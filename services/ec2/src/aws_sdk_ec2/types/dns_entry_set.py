"""Generated from Smithy shape ``com.amazonaws.ec2#DnsEntrySet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_entry

DnsEntrySet: TypeAlias = list["aws_sdk_ec2.types.dns_entry.DnsEntry"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DnsEntrySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.dns_entry

        aws_sdk_ec2.types.dns_entry.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> DnsEntrySet:
    import aws_sdk_ec2.types.dns_entry

    out: DnsEntrySet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.dns_entry.deserialize_ec2_query(child))
    return out
