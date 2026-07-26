"""Generated from Smithy shape ``com.amazonaws.docdb#VpcSecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string

VpcSecurityGroupIdList: TypeAlias = list["capo_docdb.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcSecurityGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.VpcSecurityGroupId.{n}", str(item)))


def deserialize_query(el: Element) -> VpcSecurityGroupIdList:
    out: VpcSecurityGroupIdList = []
    for child in el.findall("VpcSecurityGroupId"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: VpcSecurityGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> VpcSecurityGroupIdList:
    out: VpcSecurityGroupIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
