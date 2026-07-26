"""Generated from Smithy shape ``com.amazonaws.cloudformation#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.tag

Tags: TypeAlias = list["capo_cloudformation.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(value: Tags, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_cloudformation.types.tag

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.tag.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Tags:
    import capo_cloudformation.types.tag

    out: Tags = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Tags, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.tag

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Tags:
    import capo_cloudformation.types.tag

    out: Tags = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.tag.deserialize_query(child))
    return out
