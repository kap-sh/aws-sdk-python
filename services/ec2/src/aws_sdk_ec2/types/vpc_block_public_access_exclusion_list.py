"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusionList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion

VpcBlockPublicAccessExclusionList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_block_public_access_exclusion.VpcBlockPublicAccessExclusion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcBlockPublicAccessExclusionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vpc_block_public_access_exclusion

        aws_sdk_ec2.types.vpc_block_public_access_exclusion.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VpcBlockPublicAccessExclusionList:
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion

    out: VpcBlockPublicAccessExclusionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.vpc_block_public_access_exclusion.deserialize_ec2_query(
                child
            )
        )
    return out
