"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSecurityGroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string

CacheSecurityGroupNameList: TypeAlias = list["capo_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSecurityGroupNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.CacheSecurityGroupName.{n}", str(item)))


def deserialize_query(el: Element) -> CacheSecurityGroupNameList:
    out: CacheSecurityGroupNameList = []
    for child in el.findall("CacheSecurityGroupName"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: CacheSecurityGroupNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> CacheSecurityGroupNameList:
    out: CacheSecurityGroupNameList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
