"""Generated from Smithy shape ``com.amazonaws.autoscaling#ActivityIds``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string

ActivityIds: TypeAlias = list["capo_auto_scaling.types.xml_string.XmlString"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivityIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ActivityIds:
    out: ActivityIds = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ActivityIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ActivityIds:
    out: ActivityIds = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
