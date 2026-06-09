"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_acl_entry

NetworkAclEntryList: TypeAlias = list[
    "aws_sdk_ec2.types.network_acl_entry.NetworkAclEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAclEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.network_acl_entry

        aws_sdk_ec2.types.network_acl_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NetworkAclEntryList:
    import aws_sdk_ec2.types.network_acl_entry

    out: NetworkAclEntryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.network_acl_entry.deserialize_ec2_query(child))
    return out
