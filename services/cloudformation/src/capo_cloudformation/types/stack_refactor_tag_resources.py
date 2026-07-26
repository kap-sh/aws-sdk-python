"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorTagResources``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.tag

StackRefactorTagResources: TypeAlias = list["capo_cloudformation.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackRefactorTagResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.tag

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.tag.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackRefactorTagResources:
    import capo_cloudformation.types.tag

    out: StackRefactorTagResources = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: StackRefactorTagResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.tag

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> StackRefactorTagResources:
    import capo_cloudformation.types.tag

    out: StackRefactorTagResources = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.tag.deserialize_query(child))
    return out
