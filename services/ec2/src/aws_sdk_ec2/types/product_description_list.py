"""Generated from Smithy shape ``com.amazonaws.ec2#ProductDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

ProductDescriptionList: TypeAlias = list["aws_sdk_ec2.types.string.String"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProductDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> ProductDescriptionList:
    out: ProductDescriptionList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
