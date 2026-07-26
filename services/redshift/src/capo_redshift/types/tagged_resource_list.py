"""Generated from Smithy shape ``com.amazonaws.redshift#TaggedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.tagged_resource

TaggedResourceList: TypeAlias = list[
    "capo_redshift.types.tagged_resource.TaggedResource"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TaggedResourceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.tagged_resource

    for n, item in enumerate(value, 1):
        capo_redshift.types.tagged_resource.serialize_query(
            item, pairs, f"{prefix}.TaggedResource.{n}"
        )


def deserialize_query(el: Element) -> TaggedResourceList:
    import capo_redshift.types.tagged_resource

    out: TaggedResourceList = []
    for child in el.findall("TaggedResource"):
        out.append(capo_redshift.types.tagged_resource.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TaggedResourceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.tagged_resource

    for n, item in enumerate(value, 1):
        capo_redshift.types.tagged_resource.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TaggedResourceList:
    import capo_redshift.types.tagged_resource

    out: TaggedResourceList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.tagged_resource.deserialize_query(child))
    return out
