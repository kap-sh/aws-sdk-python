"""Generated from Smithy shape ``com.amazonaws.rds#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string

StringList: TypeAlias = list["aws_sdk_rds.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> StringList:
    out: StringList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: StringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> StringList:
    out: StringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
