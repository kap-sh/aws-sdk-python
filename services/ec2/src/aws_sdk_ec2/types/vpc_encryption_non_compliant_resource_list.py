"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionNonCompliantResourceList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource

VpcEncryptionNonCompliantResourceList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_encryption_non_compliant_resource.VpcEncryptionNonCompliantResource"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionNonCompliantResourceList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource

        aws_sdk_ec2.types.vpc_encryption_non_compliant_resource.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VpcEncryptionNonCompliantResourceList:
    import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource

    out: VpcEncryptionNonCompliantResourceList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.vpc_encryption_non_compliant_resource.deserialize_ec2_query(
                child
            )
        )
    return out
