"""Generated from Smithy shape ``com.amazonaws.sns#ActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.action

ActionsList: TypeAlias = list["capo_sns.types.action.action"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ActionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ActionsList:
    out: ActionsList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ActionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ActionsList:
    out: ActionsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
