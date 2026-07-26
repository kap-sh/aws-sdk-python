"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.region

RegionList: TypeAlias = list["capo_cloudformation.types.region.Region"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> RegionList:
    out: RegionList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: RegionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> RegionList:
    out: RegionList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
