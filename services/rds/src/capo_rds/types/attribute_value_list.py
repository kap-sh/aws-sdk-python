"""Generated from Smithy shape ``com.amazonaws.rds#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string

AttributeValueList: TypeAlias = list["capo_rds.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AttributeValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.AttributeValue.{n}", str(item)))


def deserialize_query(el: Element) -> AttributeValueList:
    out: AttributeValueList = []
    for child in el.findall("AttributeValue"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AttributeValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> AttributeValueList:
    out: AttributeValueList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
