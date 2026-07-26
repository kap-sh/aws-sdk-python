"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len19

InstanceIds: TypeAlias = list[
    "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> InstanceIds:
    out: InstanceIds = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: InstanceIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> InstanceIds:
    out: InstanceIds = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
