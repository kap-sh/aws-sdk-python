"""Generated from Smithy shape ``com.amazonaws.redshift#TaggedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.tagged_resource

TaggedResourceList: TypeAlias = list[
    "aws_sdk_redshift.types.tagged_resource.TaggedResource"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TaggedResourceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.tagged_resource

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.tagged_resource.serialize_query(
            item, pairs, f"{prefix}.TaggedResource.{n}"
        )


def deserialize_query(el: Element) -> TaggedResourceList:
    import aws_sdk_redshift.types.tagged_resource

    out: TaggedResourceList = []
    for child in el.findall("TaggedResource"):
        out.append(aws_sdk_redshift.types.tagged_resource.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TaggedResourceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.tagged_resource

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.tagged_resource.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TaggedResourceList:
    import aws_sdk_redshift.types.tagged_resource

    out: TaggedResourceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.tagged_resource.deserialize_query(child))
    return out
