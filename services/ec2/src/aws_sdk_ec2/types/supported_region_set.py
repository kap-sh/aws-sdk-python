"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.supported_region_detail

SupportedRegionSet: TypeAlias = list[
    "aws_sdk_ec2.types.supported_region_detail.SupportedRegionDetail"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SupportedRegionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.supported_region_detail

        aws_sdk_ec2.types.supported_region_detail.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SupportedRegionSet:
    import aws_sdk_ec2.types.supported_region_detail

    out: SupportedRegionSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.supported_region_detail.deserialize_ec2_query(child)
        )
    return out
