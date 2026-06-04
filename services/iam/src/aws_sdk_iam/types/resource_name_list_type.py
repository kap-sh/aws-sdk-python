"""Generated from Smithy shape ``com.amazonaws.iam#ResourceNameListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.resource_name_type

ResourceNameListType: TypeAlias = list[
    "aws_sdk_iam.types.resource_name_type.ResourceNameType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceNameListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ResourceNameListType:
    out: ResourceNameListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ResourceNameListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ResourceNameListType:
    out: ResourceNameListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
