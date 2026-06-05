"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceRequestIdList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request_id

SpotInstanceRequestIdList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_instance_request_id.SpotInstanceRequestId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotInstanceRequestIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> SpotInstanceRequestIdList:
    out: SpotInstanceRequestIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
