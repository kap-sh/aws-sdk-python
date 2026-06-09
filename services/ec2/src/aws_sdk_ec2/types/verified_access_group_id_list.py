"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_group_id

VerifiedAccessGroupIdList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> VerifiedAccessGroupIdList:
    out: VerifiedAccessGroupIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
