"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalNodeGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string

GlobalNodeGroupIdList: TypeAlias = list["aws_sdk_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalNodeGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.GlobalNodeGroupId.{n}", str(item)))


def deserialize_query(el: Element) -> GlobalNodeGroupIdList:
    out: GlobalNodeGroupIdList = []
    for child in el.findall("GlobalNodeGroupId"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: GlobalNodeGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> GlobalNodeGroupIdList:
    out: GlobalNodeGroupIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
