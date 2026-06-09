"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupReferences``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_reference

SecurityGroupReferences: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_reference.SecurityGroupReference"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupReferences, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.security_group_reference

        aws_sdk_ec2.types.security_group_reference.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SecurityGroupReferences:
    import aws_sdk_ec2.types.security_group_reference

    out: SecurityGroupReferences = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.security_group_reference.deserialize_ec2_query(child)
        )
    return out
