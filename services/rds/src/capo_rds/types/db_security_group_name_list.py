"""Generated from Smithy shape ``com.amazonaws.rds#DBSecurityGroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string

DBSecurityGroupNameList: TypeAlias = list["capo_rds.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSecurityGroupNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.DBSecurityGroupName.{n}", str(item)))


def deserialize_query(el: Element) -> DBSecurityGroupNameList:
    out: DBSecurityGroupNameList = []
    for child in el.findall("DBSecurityGroupName"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: DBSecurityGroupNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> DBSecurityGroupNameList:
    out: DBSecurityGroupNameList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
