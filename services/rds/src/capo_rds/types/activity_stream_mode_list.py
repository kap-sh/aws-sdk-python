"""Generated from Smithy shape ``com.amazonaws.rds#ActivityStreamModeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string

ActivityStreamModeList: TypeAlias = list["capo_rds.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivityStreamModeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ActivityStreamModeList:
    out: ActivityStreamModeList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ActivityStreamModeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ActivityStreamModeList:
    out: ActivityStreamModeList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
