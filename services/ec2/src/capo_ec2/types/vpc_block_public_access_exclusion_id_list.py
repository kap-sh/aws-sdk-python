"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_block_public_access_exclusion_id

VpcBlockPublicAccessExclusionIdList: TypeAlias = list[
    "capo_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcBlockPublicAccessExclusionIdList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VpcBlockPublicAccessExclusionIdList:
    out: VpcBlockPublicAccessExclusionIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
