"""Generated from Smithy shape ``com.amazonaws.autoscaling#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.tag

Tags: TypeAlias = list["capo_auto_scaling.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(value: Tags, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_auto_scaling.types.tag

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.tag.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> Tags:
    import capo_auto_scaling.types.tag

    out: Tags = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Tags, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.tag

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Tags:
    import capo_auto_scaling.types.tag

    out: Tags = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.tag.deserialize_query(child))
    return out
