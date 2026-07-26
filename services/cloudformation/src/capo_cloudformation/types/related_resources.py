"""Generated from Smithy shape ``com.amazonaws.cloudformation#RelatedResources``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.scanned_resource

RelatedResources: TypeAlias = list[
    "capo_cloudformation.types.scanned_resource.ScannedResource"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RelatedResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.scanned_resource

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.scanned_resource.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RelatedResources:
    import capo_cloudformation.types.scanned_resource

    out: RelatedResources = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.scanned_resource.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RelatedResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.scanned_resource

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.scanned_resource.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RelatedResources:
    import capo_cloudformation.types.scanned_resource

    out: RelatedResources = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.scanned_resource.deserialize_query(child))
    return out
