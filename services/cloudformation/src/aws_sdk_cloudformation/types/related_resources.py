"""Generated from Smithy shape ``com.amazonaws.cloudformation#RelatedResources``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.scanned_resource

RelatedResources: TypeAlias = list[
    "aws_sdk_cloudformation.types.scanned_resource.ScannedResource"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RelatedResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.scanned_resource

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.scanned_resource.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RelatedResources:
    import aws_sdk_cloudformation.types.scanned_resource

    out: RelatedResources = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.scanned_resource.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RelatedResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.scanned_resource

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.scanned_resource.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RelatedResources:
    import aws_sdk_cloudformation.types.scanned_resource

    out: RelatedResources = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.scanned_resource.deserialize_query(child)
        )
    return out
