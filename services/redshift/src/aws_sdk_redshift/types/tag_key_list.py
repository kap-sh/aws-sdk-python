"""Generated from Smithy shape ``com.amazonaws.redshift#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string

TagKeyList: TypeAlias = list["aws_sdk_redshift.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.TagKey.{n}", str(item)))


def deserialize_query(el: Element) -> TagKeyList:
    out: TagKeyList = []
    for child in el.findall("TagKey"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: TagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> TagKeyList:
    out: TagKeyList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
