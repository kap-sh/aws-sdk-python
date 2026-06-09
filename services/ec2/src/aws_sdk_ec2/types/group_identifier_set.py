"""Generated from Smithy shape ``com.amazonaws.ec2#GroupIdentifierSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_identifier

GroupIdentifierSet: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_identifier.SecurityGroupIdentifier"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GroupIdentifierSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.security_group_identifier

        aws_sdk_ec2.types.security_group_identifier.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> GroupIdentifierSet:
    import aws_sdk_ec2.types.security_group_identifier

    out: GroupIdentifierSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.security_group_identifier.deserialize_ec2_query(child)
        )
    return out
