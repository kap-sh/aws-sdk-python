"""Generated from Smithy shape ``com.amazonaws.cloudsearch#FieldNameList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.field_name

FieldNameList: TypeAlias = list["capo_cloudsearch.types.field_name.FieldName"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FieldNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> FieldNameList:
    out: FieldNameList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: FieldNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> FieldNameList:
    out: FieldNameList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
