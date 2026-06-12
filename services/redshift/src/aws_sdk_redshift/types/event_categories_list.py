"""Generated from Smithy shape ``com.amazonaws.redshift#EventCategoriesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string

EventCategoriesList: TypeAlias = list["aws_sdk_redshift.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventCategoriesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.EventCategory.{n}", str(item)))


def deserialize_query(el: Element) -> EventCategoriesList:
    out: EventCategoriesList = []
    for child in el.findall("EventCategory"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: EventCategoriesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> EventCategoriesList:
    out: EventCategoriesList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
